# Model-Serializer

#1 create virtual environment: python -m venv venv

#2 venv active: venv/Scripts/activate

#3 install: pip install django djangorestframework

#4 create project: django-admin startproject name .

#5 to check: python manage.py migrate python manage.py runserver

#6 configs: setting.py,urls.py

#7 create app: python manage.py startapp appname

#8 add urls.py file inside app

when add new models items then configure admin.py
also make migrate

#######################
Django Admin - Create User

py manage.py createsuperuser

Username: soton
Email address: soton@dummymail.com
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]:y

py manage.py runserver
