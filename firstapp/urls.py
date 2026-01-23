from django.urls import path
from firstapp.views import *

urlpatterns=[
    path("",index,name="index"),
]