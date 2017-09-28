from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^login/', views.loginVacation, name='loginVacation'),
    url(r'^inputVacation/', views.inputVacation, name='inputVacation'),
    url(r'^completeInput/', views.completeInput, name='completeInput'),
]
