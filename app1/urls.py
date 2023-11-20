from django.urls import path
from app1.views import *
app_name='trinadh'
urlpatterns=[
    path('datarender/',datarender,name='datarender'),
]