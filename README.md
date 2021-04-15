# django-openstreets-squirrels

# how to run this project
1. python >= 3.7 
2. install libraries
```shell
pip install -r requirements.txt
```
3. migrate database
```shell
python manage.py makekigrations maps
python manage.py migrate
```
4. run the developer server
```shell
python manage.py runserver
```
5. import and export data
import data from csv file, can be downloaded here <https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv>
```shell
python manage.py import_squirrel_data 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv
```
export data from database to a csv file
```shell
python manage.py export_squirrel_data out.csv
```


# thanks to 
1. python project <https://www.python.org/>
2. the 2018 Central Park Squirrel Census dataset <https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw>
3. OpenStreets map <https://www.openstreetmap.org/about/>
4. Leaflet an open-source JavaScript library for mobile-friendly interactive maps <https://leafletjs.com/> 
5. Django project <https://docs.djangoproject.com/>
6. map.html <https://gist.github.com/logston/0b6f2cbb928a386decd63fd616d084dd>
7. Bootstrap 4 <https://getbootstrap.com/docs/4.0/getting-started/introduction/>
8. django-bootstrap4 <https://django-bootstrap4.readthedocs.io/en/latest/>
9. DateTimePicker jQuery plugin select date and time <https://xdsoft.net/jqplugins/datetimepicker/>

# group name and section
Project Group 23, Section 1

# A list containing the UNI for each member on the team
UNIs: [jc5506, jz3279]
