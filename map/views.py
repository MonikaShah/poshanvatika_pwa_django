from django.shortcuts import render
from home.models import PictureLocation
from django.core import serializers

# Create your views here.
#def map(request):
 #   qs = PictureLocation.objects.all()
    #serialized = serializers.serialize("json", qs)
   # print(serialized[0])
  #  return render(request,'map/map.html',{'data':qs})

def new_map(request):
    return render(request,"map/new_map.html",{})