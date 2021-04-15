# coding: utf-8
from django import forms
from .models import Sight


class SightCreateForm(forms.ModelForm):
    class Meta:
        model = Sight
        fields = (
            'latitude',
            'longitude',
            'unique_squirrel_id',
            'shift',
            'date',
            'age',
            'primary_fur_color',
            'highlight_fur_color',
            'location',
            'specific_location',
            'running',
            'chasing',
            'climbing',
            'eating',
            'foraging',
            'other_activities',
            'kuks',
            'quaas',
            'moans',
            'tail_flags',
            'tail_twitches',
            'approaches',
            'indifferent',
            'runs_from',
            )

    def clean_unique_squirrel_id(self):
        error_massage_base = 'Unique Squirrel ID is comprised of "Hectare" + "Shift" + "Date" + "Hectare Squirrel Number", for example 29B-PM-1015-02.'
        unique_squirrel_id = self.cleaned_data.get('unique_squirrel_id')
        date = self.cleaned_data['date'].strftime('%m%d')
        shift_data = self.cleaned_data['shift']
        hectare, shift, d, hectare_squirrel_number = unique_squirrel_id.split('-')
        if date != d:
            raise forms.ValidationError(message=[
                error_massage_base,
                f'Date should be {date}'
                ])
        if shift_data != shift:
            raise forms.ValidationError(
                message=[
                    error_massage_base,
                    f'Shift part should be {shift_data}'])
        return unique_squirrel_id


class SightUpdateForm(forms.ModelForm):
    class Meta:
        model = Sight
        fields = (
            'latitude',
            'longitude',
            'unique_squirrel_id',
            'shift',
            'date',
            'age',)

    def clean_unique_squirrel_id(self):
        error_massage_base = 'Unique Squirrel ID is comprised of "Hectare" + "Shift" + "Date" + "Hectare Squirrel Number", for example 29B-PM-1015-02.'
        unique_squirrel_id = self.cleaned_data.get('unique_squirrel_id')
        date = self.cleaned_data['date'].strftime('%m%d')
        shift_data = self.cleaned_data['shift']
        hectare, shift, d, hectare_squirrel_number = unique_squirrel_id.split('-')
        if date != d:
            raise forms.ValidationError(message=[
                error_massage_base,
                f'Date part should be {date}'
                ])
        if shift_data != shift:
            raise forms.ValidationError(
                message=[
                    error_massage_base,
                    f'Shift part should be {shift_data}'])
        return unique_squirrel_id

