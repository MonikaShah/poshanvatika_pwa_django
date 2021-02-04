from django.urls import path, include
from . import views
urlpatterns = [
    path('basicinfo', views.basicForm, name='basicForm'),
    path('nginfo', views.NGForm, name='NGForm'),
]