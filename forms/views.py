from django.shortcuts import render
from .forms import BasicInformationForm
from django.shortcuts import redirect
# Create your views here.
def basicForm(request):
    if request.method == 'POST':
        form = BasicInformationForm(request.POST)
        if form.is_valid():
            form.save()
            print("data is saved.")
            return redirect('/forms')
    else:
        form = BasicInformationForm()
    return render(request,'forms/basic_forms.html',{})

# def basicinformation(request):

#     return render(request,'basic_information_form.html',{'form': form})


# def nutrigardeninformation(request):
#     if request.method == 'POST':
#         form = NutrigardenInformationForm(request.POST)
#         print(form)
#         if form.is_valid():
#             form.save()
#             print("data is saved.")
#             return redirect('/')
#     else:
#         form = NutrigardenInformationForm()
#     return render(request,'nutri_garden_inforamtion_form.html',{'form': form})