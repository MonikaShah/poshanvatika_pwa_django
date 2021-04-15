from django.urls import path, include
from . import views
urlpatterns = [
    #path('', views.map, name='map'),
    path('', views.new_map, name='new_map'),

]
