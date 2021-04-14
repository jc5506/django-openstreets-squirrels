# coding: utf-8
from django.urls import path


from . import views

app_name = 'maps'


urlpatterns = [
    path('', views.index, name='index'),
    path('map', views.map, name='map'),
    path('sightings', views.sighting_list, name='sighting_list'),
    ]