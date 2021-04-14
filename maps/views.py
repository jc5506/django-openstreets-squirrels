from django.shortcuts import render


def index(request):
    """home page"""
    return render(request, 'maps/index.html')


def map(request):
    """"""
    return render(request, 'maps/maps.html')
