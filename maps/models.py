from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Sight(models.Model):
    longitude = models.FloatField(
        verbose_name='Longitude',
        validators=[
            MaxValueValidator(180, message='Longitude coordinate can be as big as +180 degrees'),
            MinValueValidator(-180, message='Longitude coordinate can be as big as -180 degrees')],
        null=False, blank=False
        )
    latitude = models.FloatField(
        verbose_name='Latitude',
        validators=[
            MaxValueValidator(90, message='Longitude coordinate can be as big as +90 degrees'),
            MinValueValidator(-90, message='Longitude coordinate can be as big as -90 degrees')],
        null=False,
        blank=False)
    unique_squirrel_id = models.CharField(verbose_name='Unique Squirrel ID', max_length=16, null=False, blank=False)
    hectare = models.CharField(verbose_name='Hectare', max_length=16, null=True, blank=True)
    shift = models.CharField(verbose_name='Shift', max_length=8, null=True, blank=True),
    date = models.DateField(verbose_name='Date', null=True, blank=True)
    hectare_squirrel_number = models.PositiveIntegerField(verbose_name='Hectare Squirrel Number', null=True, blank=True)
    age = models.CharField(verbose_name='Age', max_length=16, null=True, blank=True)
    primary_fur_color = models.CharField(verbose_name='Primary Fur Color', max_length=32, null=True, blank=True)
    highlight_fur_color = models.CharField(verbose_name='Highlight Fur Color', max_length=32, null=True, blank=True)
    combination_of_primary_and_highlight_color = models.CharField(verbose_name='Combination of Primary and Highlight Color', max_length=128, null=True, blank=True)
    color_notes = models.CharField(verbose_name='Color notes', max_length=128, null=True, blank=True)
    location = models.CharField(verbose_name='Location', max_length=128, null=True, blank=True)
    above_ground_sighter_measurement = models.PositiveIntegerField(verbose_name='Above Ground Sighter Measurement', null=True, blank=True)
    Specific_Location = models.CharField(verbose_name='Specific Location', max_length=128, null=True, blank=True)
    running = models.BooleanField(verbose_name='Running', null=True, blank=True)
    chasing = models.BooleanField(verbose_name='Chasing', null=True, blank=True)
    climbing = models.BooleanField(verbose_name='Climbing', null=True, blank=True)
    eating = models.BooleanField(verbose_name='Eating', null=True, blank=True)
    foraging = models.BooleanField(verbose_name='Foraging', null=True, blank=True)
    other_activities = models.BooleanField(verbose_name='Other Activities', null=True, blank=True)
    kuks = models.BooleanField(verbose_name='Kuks', null=True, blank=True)
    quaas = models.BooleanField(verbose_name='Quaas', null=True, blank=True)
    moans = models.BooleanField(verbose_name='Moans', null=True, blank=True)
    tail_flags = models.BooleanField(verbose_name='Tail flags', null=True, blank=True)
    tail_twitches = models.BooleanField(verbose_name='Tail twitches', null=True, blank=True)
    approaches = models.BooleanField(verbose_name='Approaches', null=True, blank=True)
    indifferent = models.BooleanField(verbose_name='Indifferent', null=True, blank=True)
    runs_from = models.BooleanField(verbose_name='Runs from', null=True, blank=True)
    other_interactions = models.CharField(verbose_name='Other Interactions', max_length=128, null=True, blank=True)

    class Meta:
        ordering = '-id',
        verbose_name = 'Sight of Squirrel'
        verbose_name_plural = 'Sight if Squirrels'
