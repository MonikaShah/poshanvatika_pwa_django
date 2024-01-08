from django.urls import path, include
from . import views
from home.views import viewVatikas
urlpatterns = [
    # path('', views.map, name='map'),
    path('', viewVatikas, name='viewVatikas'),
    path('heir_map', views.heir_map, name='heir_map'),

]
