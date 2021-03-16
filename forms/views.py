from django.shortcuts import render
from .forms import BasicInformationForm, NutrigardenInformationForm, factsheetInformationForm
from django.shortcuts import redirect
# Create your views here.
def basicForm(request):
    if request.method == 'POST':
        form = BasicInformationForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.user = request.user
            instance.save()
            print("data is saved.")
            return redirect('/home')
    else:
        form = BasicInformationForm()
    return render(request,'forms/basic_forms.html',{})

# def basicinformation(request):

#     return render(request,'basic_information_form.html',{'form': form})


def NGForm(request):
    if request.method == 'POST':
        form = NutrigardenInformationForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.user = request.user
            instance.save()
            return redirect('/nginfo')
    else:
        form = NutrigardenInformationForm()
    return render(request,'forms/nutritiongarden_info.html',{'form': form})

def factsheet(request):
    if request.method == 'POST':
        form = factsheetInformationForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.user = request.user
            instance.save()
            print("data is saved.")
            return redirect('/home')
    else:
        form = factsheetInformationForm()
    return render(request,'forms/factsheet.html',{})