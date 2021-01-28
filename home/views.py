from django.shortcuts import render
import re
# from django.core.files import 
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from .models import PictureLocation
import base64
import time
# Create your views here.
def home(request):
    # if request.method == 'POST' and request.FILES['myfile']:
    global datauri
    if request.is_ajax():
        datauri = request.POST['picture']
    

    if request.method == 'POST' and not request.is_ajax():
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')

        try:
            imgstr = re.search(r'base64,(.*)', datauri).group(1)
            data = ContentFile(base64.b64decode(imgstr))
            myfile = "profile-"+time.strftime("%Y%m%d-%H%M%S")+".png"
            fs = FileSystemStorage()
            filename = fs.save(myfile, data)
            picLocation = PictureLocation.objects.create(picture_name=filename,lat=lat,lng=lng)
            picLocation.save()
            datauri = False
            del datauri
        except NameError:
            print("Image is not captured")
       
        

    return render(request,"home/home.html",{})


def contact(request):
    return render(request,"home/contact.html",{})

def about(request):
    return render(request,"home/about.html",{})