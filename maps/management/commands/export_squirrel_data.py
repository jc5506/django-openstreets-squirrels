from django.core.management.base import BaseCommand, CommandError
from maps.models import Sight
from django.conf import settings
from datetime import datetime, date
from pathlib import Path
import csv
import sys
import os

date_format = '%m%d%Y'


def format_date(v: date):
    if isinstance(v, date):
        return v.strftime(date_format)
    if v is None:
        return ''
    return str(date)


def format_boolean(v: bool):
    if v is False:
        return 'false'
    elif v is True:
        return 'true'
    return ''


class Command(BaseCommand):
    help = 'Export squirrels\' data from database to a csv file'

    def add_arguments(self, parser):
        parser.add_argument(
            'output_csv_file', type=str,
            help='Please pass in a csv file path to hold squirrels data', )

    def handle(self, *args, **options):
        output_csv_file = Path(options['output_csv_file']).resolve().absolute()
        if output_csv_file.exists():
            self.stderr.write(f'{output_csv_file} exists.')
            yes = input(f'[Y]es to overwirte, [N]o to cancel:')
            yes = yes.lower().strip()
            if yes.startswith('n'):
                sys.exit()

        if not output_csv_file.parent.exists():
            output_csv_file.mkdir(exist_ok=True)

        with open(output_csv_file, 'w', encoding='utf-8', newline='') as f:

            writer = csv.DictWriter(f, fieldnames=["X", "Y", "Unique Squirrel ID", "Hectare", "Shift", "Date", "Hectare Squirrel Number", "Age", "Primary Fur Color", "Highlight Fur Color", "Combination of Primary and Highlight Color", "Color notes", "Location", "Above Ground Sighter Measurement", "Specific Location", "Running", "Chasing", "Climbing", "Eating", "Foraging", "Other Activities", "Kuks", "Quaas", "Moans", "Tail flags", "Tail twitches", "Approaches", "Indifferent", "Runs from", "Other Interactions", "Lat/Long"],)
            writer.writeheader()

            t = 0
            for sight in Sight.objects.order_by('id').all():
                row = {
                    "X": sight.longitude,
                    "Y": sight.latitude,
                    "Unique Squirrel ID": sight.unique_squirrel_id,
                    "Hectare": sight.hectare,
                    "Shift": sight.shift,
                    "Date": format_date(sight.date),
                    "Hectare Squirrel Number": sight.hectare_squirrel_number,
                    "Age": sight.age,
                    "Primary Fur Color": sight.primary_fur_color,
                    "Highlight Fur Color": sight.highlight_fur_color,
                    "Combination of Primary and Highlight Color": sight.combination_of_primary_and_highlight_color,
                    "Color notes": sight.color_notes,
                    "Location": sight.location,
                    "Above Ground Sighter Measurement": sight.above_ground_sighter_measurement,
                    "Specific Location": sight.specific_location,
                    "Running": format_boolean(sight.running),
                    "Chasing": format_boolean(sight.chasing),
                    "Climbing": format_boolean(sight.climbing),
                    "Eating": format_boolean(sight.eating),
                    "Foraging": format_boolean(sight.foraging),
                    "Other Activities": sight.other_activities,
                    "Kuks": format_boolean(sight.kuks),
                    "Quaas": format_boolean(sight.quaas),
                    "Moans": format_boolean(sight.moans),
                    "Tail flags": format_boolean(sight.tail_flags),
                    "Tail twitches": format_boolean(sight.tail_twitches),
                    "Approaches": format_boolean(sight.approaches),
                    "Indifferent": format_boolean(sight.indifferent),
                    "Runs from": format_boolean(sight.runs_from),
                    "Other Interactions": sight.other_interactions,
                    "Lat/Long": f'POINT ({sight.longitude} {sight.latitude})'
                    }
                writer.writerow(row)
                t += 1
                self.stdout.write(f'{sight.longitude}/{sight.latitude}/{sight.unique_squirrel_id} exported', ending='\n')
            self.stdout.write(f'{t} rows exported in total')

