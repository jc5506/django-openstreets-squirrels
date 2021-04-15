from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Sight
from django.core.paginator import PageNotAnInteger, InvalidPage, EmptyPage, Paginator
from .forms import SightCreateForm, SightUpdateForm
from django.contrib import messages


def index(request):
    """home page"""
    return render(request, 'maps/index.html')


def map(request):
    """"""
    data = []
    t = 0
    for sight in Sight.objects.all():
        _ = {'latitude': sight.latitude, 'longitude': sight.longitude}
        if _ in data:
            continue
        data.append(_)
        t += 1
        if t >= 100:
            break
    return render(request, 'maps/maps.html', context=dict(sightings=data))


def sighting_list(request):
    """"""
    page = request.GET.get('page', '1')
    try:
        page = int(page)
    except (TypeError, ValueError):
        page = 1
    per_page = request.GET.get('per_page', 15)
    try:
        per_page = int(per_page)
    except (TypeError, ValueError):
        per_page = 15
    ls = Sight.objects.all()
    paginator = Paginator(object_list=ls, per_page=per_page)
    try:
        ls = paginator.page(page)
    except PageNotAnInteger:
        ls = paginator.page(1)
    except EmptyPage:
        ls = paginator.page(paginator.num_pages)
    if paginator.num_pages <= 2:
        page_no_ls = []
    if paginator.num_pages <= 5:
        page_no_ls = list(range(paginator.num_pages))
    else:
        if page <= 5:
            start = 1
            end = 11
        elif page >= paginator.num_pages - 5:
            start = paginator.num_pages - 5
            end = paginator.num_pages + 1
        else:
            start = page - 5
            end = page + 5

        page_no_ls = []
        for i in range(start, end):
            if i < 1:
                continue
            if i > paginator.num_pages:
                break
            page_no_ls.append(i)

    return render(request, 'maps/sighting_list.html', context=dict(
        ls=ls, page=page, per_page=per_page, page_no_ls=page_no_ls, title='Squirrels Sightings',
    ))


def sight_create(request):
    if request.method == 'POST':
        form = SightCreateForm(request.POST)
        if form.is_valid():
            sight = form.save(commit=False)
            hectare, shift, d, hectare_squirrel_number = sight.unique_squirrel_id.split('-')
            sight.hectare_squirrel_number = int(hectare_squirrel_number)
            sight.save()
            messages.success(request, 'Squirrel sighting created')
            return redirect(reverse('maps:sighting_list'))
    else:
        form = SightCreateForm()

    return render(request, 'maps/sighting_create.html', context={'form': form})


def sight_update(request, unique_squirrel_id):
    sight = get_object_or_404(klass=Sight, unique_squirrel_id=unique_squirrel_id)
    if request.method == 'POST':
        form = SightUpdateForm(data=request.POST, instance=sight)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated')
    else:
        form = SightUpdateForm(instance=sight)
    return render(request, 'maps/sighting_update.html', context=dict(
        title=f'Update {unique_squirrel_id}', form=form
        ))
