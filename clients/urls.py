#-*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views
from django.contrib import admin
from .views import DriverView, RequestView

# namespace
app_name = 'clients'

urlpatterns = [

    path('bookDriver/',RequestView.as_view(), name='bookDriver'),

    path('getAllRequests/',RequestView.as_view(),name='getAllRequests'),

    path('getDriverRequests/',RequestView.as_view(),name='geDriverRequests'),

    path('findNearDriver/',DriverView.as_view(),name='findNearDriver'),

]