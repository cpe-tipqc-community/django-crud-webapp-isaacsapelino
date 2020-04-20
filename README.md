# django-crud-webapp-isaacsapelino

The following materials here are the source code for the crud webapp made by Isaac Sapelino.

The following packages that was used: 
## Requirements
* asgiref                    3.2.7
* bcrypt                     3.1.7
* cffi                       1.14.0
* Django                     3.0.5
* django-crispy-forms        1.9.0
* django-password-validation 0.1.1
* Pillow                     7.1.1
* pip                        19.2.3
* pycparser                  2.20
* pytz                       2019.3
* setuptools                 41.2.0
* six                        1.14.0
* sqlparse                   0.3.1



### Initialization Notes
On default, I have written a JSON file for the categories that will be needing to be upload in django.
Use the command ```python manage.py loaddata test-db.json``` to upload the fixtures.

## Initialization Process
To setup the webapp, we need to initialize django for making our db.sqlite3 

1. Python migrations
Do ```python manage.py makemigrations``` to make migrations the needed models for our web app..

2. Python migrate
Do ```python manage.py migrate``` to begin puting the created django migrations to the sqlite.

3. Loading the test-db
Do ```python manage.py loaddata test-db.json``` to upload the necessary fixtures

4. Start django server 
After doing the process of initializing the database we can now run the server.
Do ```python manage.py runserver```
