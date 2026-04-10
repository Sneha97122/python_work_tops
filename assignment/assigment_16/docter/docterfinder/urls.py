from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add/', views.add_doctor),
    path('delete/<int:id>/', views.delete_doctor),
]
