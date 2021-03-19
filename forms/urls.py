from django.urls import path, include
from . import views
urlpatterns = [
    path('basicinfo', views.basicForm, name='basicForm'),
    path('nginfo', views.NGForm, name='NGForm'),
    path('factsheet', views.factsheet, name='factsheet'),
    path('factsheet_dynamic', views.factsheet_dynamic, name='factsheet_dynamic'),
    path('financial', views.financial, name='financial'),


]