from django.urls import path
from app2.views import *
app_name='trinadh'
urlpatterns=[
    path('submit/',submit,name='submit'),
]