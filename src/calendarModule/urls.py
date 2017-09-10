from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.viewCalendar, name='viewCalendar')
]
