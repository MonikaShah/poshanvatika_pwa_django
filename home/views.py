from django.shortcuts import render
import re
# from django.core.files import 
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from .models import PictureLocation
import base64
import time

#login dependacies
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


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request,"home/login_form.html",context={"form":form})


def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')
    
def factsheet(request):
	return render(request,"home/factsheet.html",{})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            messages.success(request, f"New account created: {username}")
            user = authenticate(username=username, password=raw_password)
            auth.login(request,user)
            print("registeration Successful")
            return redirect('/')
        else:
            
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            return render(request,"home/signup.html",{"form":form})
    else:
        form = UserCreationForm()
    return render(request, 'home/signup.html', {'form': form})
