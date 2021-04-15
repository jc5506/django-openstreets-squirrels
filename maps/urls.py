# coding: utf-8
from django.urls import path, re_path

from . import views

app_name = 'maps'


urlpatterns = [
    path('', views.index, name='index'),
    path('map', views.map, name='map'),
    path('sightings', views.sighting_list, name='sighting_list'),
    path('sightings/add', views.sight_create, name='sighting_create'),
    re_path(r'^sightings/(?P<unique_squirrel_id>[0-9]{1,2}[A-I]-[AP]M-\d{4}-\d+)$', views.sight_update, name='sighting_update'),
    ]