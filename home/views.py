from django.shortcuts import render
from .forms import NewUserForm
import re
# from django.core.files import 
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from .models import PictureLocation
import base64
import time

#login dependacies
from django.contrib.auth import login, authenticate #add this
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from .forms import UploadPictureForm
# Create your views here.
def home(request):
    form = UploadPictureForm()
    global datauri
    if request.is_ajax():
        datauri = request.POST['picture']
    

    if request.method == 'POST' and not request.is_ajax():
        form = UploadPictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        # lat = request.POST.get('lat')
        # lng = request.POST.get('lng')

        # try:
        #     imgstr = re.search(r'base64,(.*)', datauri).group(1)
        #     data = ContentFile(base64.b64decode(imgstr))
        #     myfile = "profile-"+time.strftime("%Y%m%d-%H%M%S")+".png"
        #     fs = FileSystemStorage()
        #     filename = fs.save(myfile, data)
        #     picLocation = PictureLocation.objects.create(user=request.user,picture_name=filename,lat=lat,lng=lng)
        #     picLocation.save()
        #     datauri = False
        #     del datauri
        # except NameError:
        #     print("Image is not captured")
       
        

    return render(request,"home/home.html",{'form':form})


def contact(request):
    return render(request,"home/contact.html",{})

def about(request):
    return render(request,"home/about.html",{})

def myPoshan(request):
    return render(request,"home/myPoshan.html",{})

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
