from django.contrib import admin
from . import models


@admin.register(models.Sight)
class SightAdmin(admin.ModelAdmin):
    list_display = 'id', 'longitude', 'latitude', 'unique_squirrel_id', 'shift', 'date', 'age'
    list_display_links = 'unique_squirrel_id',
    search_fields = 'unique_squirrel_id',
