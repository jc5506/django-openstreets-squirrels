from django.shortcuts import render
from .models import Sight
# Create your views here.


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