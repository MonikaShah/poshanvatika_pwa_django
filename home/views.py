from django.core.exceptions import TooManyFieldsSent
from django.shortcuts import render
from .forms import NewUserForm
import re
# from django.core.files import 
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
import base64
import time

#login dependacies
from django.contrib.auth import login, authenticate #add this
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from .forms import UploadPictureForm, UploadWellPictureForm
from .models import UploadWellPictureModel, UploadPictureModel
# Create your views here.

#for rendering the data from database
def viewLayers(request):
    wells = UploadWellPictureModel.objects.all()
    vatikas = UploadPictureModel.objects.all()
    # captwells = WellPictureLocationModel.objects
    context = {'wells': wells, 'vatikas': vatikas}
    return render(request, 'home/viewLayers.html', context )
    #return render(request, 'map/map.html', context)

def captwellpic(request):
    form = UploadWellPictureForm()
    global datauri
    if request.is_ajax():
        datauri = request.POST['picture']
    
    if request.method == 'POST' and not request.is_ajax():
        form = UploadWellPictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        name = request.POST.get('name')
        well_nm = request.POST.get('well_nm')
        radius = request.POST.get('radius')
        depth = request.POST.get('depth')
        level = request.POST.get('level')
        village = request.POST.get('village')
        district = request.POST.get('district')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        try:
            imgstr = re.search(r'base64,(.*)', datauri).group(1)
            data = ContentFile(base64.b64decode(imgstr))
            myfile = "WellPics/profile-"+time.strftime("%Y%m%d-%H%M%S")+".png"
            fs = FileSystemStorage()
            filename = fs.save(myfile, data)
            picLocation = UploadWellPictureModel.objects.create(picture=filename, name=name, well_nm=well_nm, radius=radius, depth=depth, level=level, village=village, district=district, state=state,pincode=pincode, lat=lat, lng=lng)
            picLocation.save()
            datauri = False
            datauri= False
            del datauri
        except NameError:
            print("Image is not captured")
    else:
        form = UploadWellPictureForm()
    return render(request,'home/captureWellPic.html',{})

def uploadwellpic(request):
    if request.method == 'POST':
        form = UploadWellPictureForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.user = request.user
            instance.save()
            print("data is saved.")
            return redirect('/captwellpic')
    else:
        form = UploadWellPictureForm()
    return render(request,'home/uploadWellPic.html',{})

def captvatikapic(request):
    form = UploadPictureForm()
    global datauri
    if request.is_ajax():
        datauri = request.POST['picture']
    
    if request.method == 'POST' and not request.is_ajax():
        form = UploadPictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        name = request.POST.get('name')
        nutri_nm = request.POST.get('nutri_nm')
        area = request.POST.get('area')
        village = request.POST.get('village')
        district = request.POST.get('district')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        try:
            imgstr = re.search(r'base64,(.*)', datauri).group(1)
            data = ContentFile(base64.b64decode(imgstr))
            myfile = "VatikaPics/profile-"+time.strftime("%Y%m%d-%H%M%S")+".png"
            fs = FileSystemStorage()
            filename = fs.save(myfile, data)
            picLocation = UploadPictureModel.objects.create(picture=filename, name=name, nutri_nm=nutri_nm, area=area, village=village, district=district, state=state,pincode=pincode, lat=lat, lng=lng)
            picLocation.save()
            datauri = False
            datauri= False
            del datauri
        except NameError:
            print("Image is not captured")
    else:
        form = UploadPictureForm()
    return render(request,'home/captureVatikaPic.html',{})

    
def uploadvatikapic(request):
    if request.method == 'POST':
        form = UploadPictureForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.user = request.user
            instance.save()
            print("data is saved.")
            return redirect('/captvatikapic')
    else:
        form = UploadPictureForm()
    return render(request,"home/uploadVatikaPic.html",{'form': form})


def contact(request):
    return render(request,"home/contact.html",{})

def about(request):
    return render(request,"home/about.html",{})

def myPoshan(request):
    return render(request,"home/myPoshan.html",{})

def news(request):
    return render(request,"home/news.html",{})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="home/login.html", context={"login_form":form})


def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')
    


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user, backend='django.contrib.auth.backends.ModelBackend')
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="home/register.html", context={"register_form":form})
