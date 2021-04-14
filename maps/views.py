from django.shortcuts import render
from .models import Sight
from django.core.paginator import PageNotAnInteger, InvalidPage, EmptyPage, Paginator


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
        page_no_ls = []
        for i in range(page-5, page+5):
            if i < 1:
                continue
            if i > paginator.num_pages:
                break
            page_no_ls.append(i)

    return render(request, 'maps/sighting_list.html', context=dict(
        ls=ls, page=page, per_page=per_page, page_no_ls=page_no_ls
    ))