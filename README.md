# Simple-search-application-with-django
This is a developer search app made using the python framework Django. It has a index/home page where user can select the type of developer they want to search. The user has 3 options: 1. search developer who can write ruby or javascript or both of them, 2. search developer who can write ruby or javascript or both of them and speak Japanese, 3. search developer who can speak Japanese.

This project also have an API system through which an user can get all developer info including the developer's known programming languages and normal languages. The user can also post, put and delete developers through api calls.

To run the project user need to have python, django and django-rest-framework install in the running environment.

###### To install django, run (without quotation):
        "pip install django"
              
###### To install django-rest-framework, run (without quotation):
        "pip install djangorestframework"
        
        
## Project Database
The project uses mysql to connect to the database. For that user must have mysqlClient intalled in environment. The db name that was used in the project is 'search_app'.

###### To install django-seed, run:
        pip install mysqlclient

The project has some seed dumy data for 100+ developers, 7 programming languages and 4 language codes. For seeding the random developers, user must have django_seed module installed in the environment.
        
###### To install django-seed, run (without quotation):
        "pip install django-seed"
               
###### For migration, run in the project root directory(without quotation):
        "py manage.py migrate"
        
by running the migration, the seed data will be loaded into the database and the developers will be randomly be connected to both programming languages and languages.
