# coding: utf-8
from django import forms
from .models import Sight, unique_squirrel_id_validate

error_massage_base = 'Unique Squirrel ID is comprised of "Hectare" + "Shift" + "Date" + "Hectare Squirrel Number", for example 29B-PM-1015-02.'


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
        unique_squirrel_id = self.cleaned_data.get('unique_squirrel_id')
        unique_squirrel_id_validate(unique_squirrel_id)
        return unique_squirrel_id

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age not in ['Adult', 'Juvenile']:
            raise forms.ValidationError(['Age is required', 'Ether Adult or Juvenile'])
        return age

    def clean_shift(self):
        shift_data = self.cleaned_data.get('shift')
        if shift_data not in ['PM', 'AM']:
            raise forms.ValidationError(['Shift is required', 'Ether PM or AM'])
        return shift_data

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date is None:
            raise forms.ValidationError(['Date is required', 'The date format is Y-m-d, like 2021-04-15'])
        return date

    def clean(self):
        unique_squirrel_id = self.cleaned_data.get('unique_squirrel_id')
        hectare, shift, d, hectare_squirrel_number = unique_squirrel_id.split('-')
        date = self.cleaned_data.get('date')
        shift_data = self.cleaned_data.get('shift')
        error_ls = []

        if date:
            date = date.strftime('%m%d')
            if date != d:
                error_ls.append(f'Date part should be {date}')
        if shift_data:
            if shift_data and shift_data != shift:
                error_ls.append(f'Shift part should be {shift_data}')

        if error_ls:
            raise forms.ValidationError(
                [error_massage_base] + error_ls
                )


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
        unique_squirrel_id = self.cleaned_data.get('unique_squirrel_id')
        unique_squirrel_id_validate(unique_squirrel_id)
        return unique_squirrel_id

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age not in ['Adult', 'Juvenile']:
            raise forms.ValidationError(['Age is required', 'Ether Adult or Juvenile'])
        return age

    def clean_shift(self):
        shift_data = self.cleaned_data.get('shift')
        if shift_data not in ['PM', 'AM']:
            raise forms.ValidationError(['Shift is required', 'Ether PM or AM'])
        return shift_data

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date is None:
            raise forms.ValidationError(['Date is required', 'The date format is Y-m-d, like 2021-04-15'])
        return date

    def clean(self):
        unique_squirrel_id = self.cleaned_data.get('unique_squirrel_id')
        hectare, shift, d, hectare_squirrel_number = unique_squirrel_id.split('-')
        date = self.cleaned_data.get('date')
        shift_data = self.cleaned_data.get('shift')
        error_ls = []

        if date:
            date = date.strftime('%m%d')
            if date != d:
                error_ls.append(f'Date part should be {date}')
        if shift_data:
            if shift_data and shift_data != shift:
                error_ls.append(f'Shift part should be {shift_data}')

        if error_ls:
            raise forms.ValidationError([error_massage_base] + error_ls)

