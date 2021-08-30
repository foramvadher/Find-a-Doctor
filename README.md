# Find-a-Doctor
This is a task for a company which required a backend for saving and retrival of Doctor's data according to search.

I found it really challenging for me to learn Django and implement the task within a few days, it was fun though let's get started.

## Step 1 : Set up Django

### 1.1 Install Django
First we'll install Django
```shell script
pip install django 
```
### 1.2 Create a Project
Now after successful installation let's create a project
```shell script
django-admin startproject necktieTask
```
The above code creates a folder of our project name 'neckTie', which has everything to run a Django site
### 1.3 Create an API Application for project
```shell script
python manage.py startapp doctorAPI
```
Now we need to register the above API into our project
So add our application name to necktie/setting.py file
```python script
INSTALLED_APPS = [
    'doctorAPI',
    ... # Do not edit other INSTALLED_APPS there
]
```
## Step 2 : Creat Models in Django
We'll create Models in Django app that'll be managed by Django ORM
### 2.1 Edit DoctorAPI/models.py
Analyse the problem and optimise the tables creating the ER diagrams
<img style="align:left" width="604" height="400" src="https://user-images.githubusercontent.com/64018909/131244701-47619696-c580-4971-86cb-76beb55180fb.png">

Now finally, write down the models in models.py file in your application folder

https://github.com/foramvadher/Find-a-Doctor/blob/main/necktieTask/doctorAPI/models.py
### 2.2 Make migrations
After any change made to the models we need to tell Django to migrate those changes. To do so we run the following commands
```shell script
python manage.py makemigrations
python manage.py migrate
```
### 2.3 Registering models in admin.py
All the models created in the models.py need to be registered in admin.py file 
```python script
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Contact)
admin.site.register(Language)
admin.site.register(District)
admin.site.register(Specialization)
admin.site.register(Availability)
```
### 2.4 Running server for admin
Create a superuser for your application
```shell scrpit
python manage.py createsuperuser --email admin@example.com --username admin
```
Now we can run the server and add data from admin site
Run server using this command:
```shell script
python manage.py runserver
```
Finally open the admin site:
http://localhost:8000/admin

## 3 Set up Django REST Framework
```shell script
pip install djangorestframework
```
Also register this to our INSTALLED_APPS in neckTie/settings.py files
```python script
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```
### 4 Serialize the models
To convert the Model output to JSON we need to serialize using default serializers.

For that we create a new file serializers.py into the DoctorAPI folder and add the data

https://github.com/foramvadher/Find-a-Doctor/blob/main/necktieTask/doctorAPI/serializers.py

### 5 Create Views for display
To view our data in understandable format from the DB, we need to query the DB and then pass it to the serializers that we just created to render it to JSON format.

We have to pass that database queryset into the serializer we just created, so that it gets converted into JSON and rendered

So we'll write the code to DoctorAPI/views.py file

https://github.com/foramvadher/Find-a-Doctor/blob/main/necktieTask/doctorAPI/views.py

## 6 Set urls for access
Finally at the last step we'll attach the views to our urls so we can access them using browser

### 6.1 Set API urls
Edit API urls :

https://github.com/foramvadher/Find-a-Doctor/blob/main/necktieTask/doctorAPI/urls.py

the above can alse be set without using routers, but routers does this all on its own:
```python script 
from . import views
from django.conf.urls import url 

urlpatterns = [ 
    url(r'^doctor/$', views.DoctorsViewSet.as_view({'get':'list','post':'create'}),
    url(r'^doctor/(?P<id>[0-9]+)$', views.DoctorsViewSet.as_view({'get':'list'}),
]
```
### 6.2 Set site urls
Edit urls in necktieTask folder and include the above file's urls to get them registered

https://github.com/foramvadher/Find-a-Doctor/blob/main/necktieTask/necktieTask/urls.py

## 7 Test APIs 
Now we can run the API in browsers from localhost

Try testing following urls:
- List of all doctors
  
  http://localhost:8000/doctor/

- Search a doctor by ID
  
  http://localhost:8000/doctor/2
  
- List all doctors with filters

  http://localhost/doctor?dist=Islands&price=1500
  
  http://localhost/doctor?price=1500&lang=english&category=general  
  
- Post one or many doctors

  http://localhost:8000/doctor/
  
  Post format
  ```json script
  [
    {
        "docID": 1,
        "name": "test Doctor",
        "specialization": {
            "spName": "Obstetrics & Gynaecology"
        },
        "contacts": [
            "1234567890"
        ],
        "eMail": "testemail@mail",
        "qualification": "PHD",
        "languages": [
            "English",
            "Chinese"
        ],
        "addr": "test address",
        "dist": {
            "distName": "Kwai Tsing",
            "region": "NT"
        },
        "price": 1200,
        "priceRemarks": "inclusive all taxes",
        "availability": [
            {
                "day": "MON",
                "startTime": "06:00:00",
                "endTime": "18:00:00"
            },
            {
                "day": "TUE",
                "startTime": "06:00:00",
                "endTime": "18:00:00"
            }
        ],
        "holidayRemarks": "no holiday"
    },
    ......................
  ]
  ```
