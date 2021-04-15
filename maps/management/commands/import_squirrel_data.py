from django.core.management.base import BaseCommand, CommandError
from maps.models import Sight
from django.conf import settings
from datetime import datetime
from pathlib import Path
import csv
import sys
import os

date_format = '%m%d%Y'


def parse_date(v: str):
    try:
        return datetime.strptime(v, date_format)
    except ValueError:
        pass


def parse_boolean(v: str):
    if v == 'false':
        return False
    elif v == 'true':
        return True
    return


class Command(BaseCommand):
    help = 'Import squirrels\' data from csv file to database'

    def add_arguments(self, parser):
        parser.add_argument(
            'input_csv_file', type=str,
            help='Please pass in a csv file with squirrels data you want to import', )

    def handle(self, *args, **options):
        input_csv_file = Path(options['input_csv_file']).resolve().absolute()
        if not input_csv_file.exists():
            self.stderr.write(
                f'Error occurred while trying to import data. '
                f'"{input_csv_file}" can not be found.'
                f' Please pass in a csv file with squirrels data.')
            sys.exit(1)
        with open(input_csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, fieldnames=["X", "Y", "Unique Squirrel ID", "Hectare", "Shift", "Date", "Hectare Squirrel Number", "Age", "Primary Fur Color", "Highlight Fur Color", "Combination of Primary and Highlight Color", "Color notes", "Location", "Above Ground Sighter Measurement", "Specific Location", "Running", "Chasing", "Climbing", "Eating", "Foraging", "Other Activities", "Kuks", "Quaas", "Moans", "Tail flags", "Tail twitches", "Approaches", "Indifferent", "Runs from", "Other Interactions", "Lat/Long"],)
            t = -1
            for item in reader:
                if t == -1:
                    t += 1
                    continue

                longitude = item['X']
                latitude = item['Y']

                unique_squirrel_id = item['Unique Squirrel ID']
                hectare = item['Hectare']
                shift = item['Shift']  # fix remove ",", cause comma make this value tuple
                date = parse_date(item['Date'])

                hectare_squirrel_number = item['Hectare Squirrel Number']
                age = item['Age']
                primary_fur_color = item['Primary Fur Color']
                highlight_fur_color = item['Highlight Fur Color']
                # combination_of_primary_and_highlight_color = item['Combination of Primary and Highlight Color']
                color_notes = item['Color notes']
                location = item['Location']
                above_ground_sighter_measurement = item['Above Ground Sighter Measurement']
                specific_location = item['Specific Location']
                running = parse_boolean(item['Running'])
                chasing = parse_boolean(item['Chasing'])
                climbing = parse_boolean(item['Climbing'])
                eating = parse_boolean(item['Eating'])
                foraging = parse_boolean(item['Foraging'])
                other_activities = item['Other Activities']
                kuks = parse_boolean(item['Kuks'])
                quaas = parse_boolean(item['Quaas'])
                moans = parse_boolean(item['Moans'])
                tail_flags = parse_boolean(item['Tail flags'])
                tail_twitches = parse_boolean(item['Tail twitches'])
                approaches = parse_boolean(item['Approaches'])
                indifferent = parse_boolean(item['Indifferent'])
                runs_from = parse_boolean(item['Runs from'])
                other_interactions = item['Other Interactions']
                Sight.objects.create(
                    longitude=longitude, latitude=latitude,
                    unique_squirrel_id=unique_squirrel_id,
                    hectare=hectare, shift=shift, date=date,
                    hectare_squirrel_number=hectare_squirrel_number, age=age, primary_fur_color=primary_fur_color,
                    highlight_fur_color=highlight_fur_color,
                    # combination_of_primary_and_highlight_color=combination_of_primary_and_highlight_color,
                    color_notes=color_notes, location=location,
                    above_ground_sighter_measurement=above_ground_sighter_measurement,
                    specific_location=specific_location, running=running, chasing=chasing, climbing=climbing,
                    eating=eating, foraging=foraging, other_activities=other_activities, kuks=kuks, quaas=quaas,
                    moans=moans, tail_flags=tail_flags, tail_twitches=tail_twitches, approaches=approaches,
                    indifferent=indifferent, runs_from=runs_from, other_interactions=other_interactions,
                    )
                t += 1
                self.stdout.write(f'{longitude}/{latitude}/{unique_squirrel_id} imported', ending='\n')
            self.stdout.write(f'{t} rows imported in total')

