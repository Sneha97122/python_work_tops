from django.urls import path
from docterfinder.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home,name="home"),
    path('doctors/',doctor_list,name="doctors"),
    path('contact/',contact,name="contact"),
    path('login/', auth_views.LoginView.as_view(), name='login'),   
]