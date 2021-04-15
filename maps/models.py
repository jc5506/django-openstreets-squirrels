from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from datetime import datetime
import re


hectare_choices = []

for r in range(1, 42+1):
    for s in range(ord('A'), ord('I')+1):
        hectare_choices.append(
            (f'{r}{chr(s)}', f'{r}{chr(s)}')
            )
shift_choices = [
    ('AM', 'AM'),
    ('PM', 'PM'),
    ]


age_choices = [
    ('Adult', 'Adult'),
    ('Juvenile', 'Juvenile'),
    ]

color_choices = [
    ('Gray', 'Gray'),
    ('Cinnamon', 'Cinnamon'),
    ('Black', 'Black'),
    ]
location_choices = [
    ('Ground Plane', 'Ground Plane'),
    ('Above Ground', 'Above Ground'),
    ]


def unique_squirrel_id_validate(s: str):
    """"""
    error_massage_base = 'Unique Squirrel ID is comprised of "Hectare" + "Shift" + "Date" + "Hectare Squirrel Number", for example 29B-PM-1015-02.'
    try:
        hectare, shift, d, hectare_squirrel_number = s.split('-')
    except ValueError:
        raise ValidationError(message=error_massage_base)

    if hectare not in [i for i, j in hectare_choices]:
        raise ValidationError(message=[
            error_massage_base,
            f'Hectare part should be from 1A-42I.',
            'The digits part is 1-42, and the letter part is from A-I',
            ])
    if shift not in ['AM', 'PM']:
        raise ValidationError(
            message=[error_massage_base, f'Shift part should be one of AM|PM'])
    try:
        if len(d) != 4:
            raise ValueError
        datetime.strptime(d, '%m%d')
    except ValueError:
        raise ValidationError(message=[
            error_massage_base,
            f'Date part should be in %m%d format, for example 1014'
            ])
    if not re.findall('^\d+$', hectare_squirrel_number):
        raise ValidationError(message=[error_massage_base, f'Hectare Squirrel Number part should digits, for example 01'])
    return True


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
    unique_squirrel_id = models.CharField(verbose_name='Unique Squirrel ID', max_length=32, null=False, blank=False,
                                          validators=[unique_squirrel_id_validate], unique=True, db_index=True)

    hectare = models.CharField(verbose_name='Hectare', max_length=16, null=True, blank=True, choices=hectare_choices)
    shift = models.CharField(verbose_name='Shift', max_length=8, null=True, blank=True, choices=shift_choices)
    date = models.DateField(verbose_name='Date', null=True, blank=True)
    hectare_squirrel_number = models.PositiveIntegerField(verbose_name='Hectare Squirrel Number', null=True, blank=True)
    age = models.CharField(verbose_name='Age', max_length=16, null=True, blank=True, choices=age_choices)
    primary_fur_color = models.CharField(verbose_name='Primary Fur Color', max_length=32, null=True, blank=True, choices=color_choices)
    highlight_fur_color = models.CharField(verbose_name='Highlight Fur Color', max_length=32, null=True, blank=True, choices=color_choices)
    # combination_of_primary_and_highlight_color = models.CharField(verbose_name='Combination of Primary and Highlight Color', max_length=128, null=True, blank=True)
    color_notes = models.CharField(verbose_name='Color notes', max_length=128, null=True, blank=True)
    location = models.CharField(verbose_name='Location', max_length=128, null=True, blank=True, choices=location_choices)
    above_ground_sighter_measurement = models.CharField(verbose_name='Above Ground Sighter Measurement', max_length=64, null=True, blank=True)
    specific_location = models.CharField(verbose_name='Specific Location', max_length=128, null=True, blank=True)
    running = models.BooleanField(verbose_name='Running', null=True, blank=True)
    chasing = models.BooleanField(verbose_name='Chasing', null=True, blank=True)
    climbing = models.BooleanField(verbose_name='Climbing', null=True, blank=True)
    eating = models.BooleanField(verbose_name='Eating', null=True, blank=True)
    foraging = models.BooleanField(verbose_name='Foraging', null=True, blank=True)
    other_activities = models.CharField(verbose_name='Other Activities', max_length=128, null=True, blank=True)
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
        verbose_name_plural = 'Sight of Squirrels'

    def __str__(self):
        return self.unique_squirrel_id

    @property
    def combination_of_primary_and_highlight_color(self):
        return f'{self.primary_fur_color or ""}+{self.highlight_fur_color or ""}'






