from django.forms import ModelForm
from .models import UploadPictureModel, UploadWellPictureModel, WellPictureLocationModel, PictureLocation
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


# class UploadPictureForm(ModelForm):
#     picture = forms.ImageField(label='')
#     name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter Your name','class': 'upload_field'}))
#     nutri_nm = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter Name Of Your Nutri garden','class': 'upload_field'}))
#     area = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter Area Name','class': 'upload_field'}))
#     village = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter village Name','class': 'upload_field'}))
#     district = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter district Name','class': 'upload_field'}))
#     state = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter state Name','class': 'upload_field'}))
#     pincode = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter pincode','class': 'upload_field'}))
#     class Meta:
#             model = UploadPicture
#             fields = '__all__'

class PictureLocationForm(forms.ModelForm):
    class Meta:
        model = PictureLocation
        fields = ('picture_name','name','nutrinm','lat','lng')

class UploadPictureForm(forms.ModelForm):
    class Meta:
        model = UploadPictureModel
        fields = ('picture','name','nutri_nm','area','village','district','state','pincode')

class WellPictureLocationForm(forms.ModelForm):
    class Meta:
        model= WellPictureLocationModel
        fields = ('picture_name','name','wellnm','radius','depth','level','lat','lng')

class UploadWellPictureForm(forms.ModelForm):
    class Meta:
        model = UploadWellPictureModel
        fields = ('picture','name','well_nm','radius','depth','level','village','district','state','pincode', 'lat', 'lng')
# class UploadWellPictureForm(ModelForm):
#     picture = forms.ImageField(label='')
#     name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter Your name','class': 'upload_field'}))
#     well_nm = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter Name Of the Well (if any)','class': 'upload_field'}))
#     radius = forms.IntegerField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter radius of the well','class': 'upload_field'}))
#     depth = forms.IntegerField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter depth of the well','class': 'upload_field'}))
#     level = forms.IntegerField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter water levels of the well','class': 'upload_field'}))
#     village = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter village Name','class': 'upload_field'}))
#     district = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter district Name','class': 'upload_field'}))
#     state = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter state Name','class': 'upload_field'}))
#     pincode = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter pincode','class': 'upload_field'}))
#     class Meta:
#             model = UploadWellPicture
#             fields = '__all__'

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None      
    
    class Meta:
        model=User
        fields = ('username', 'email', 'password1', 'password2')
        def save(self, commit=True):
            user = super(NewUserForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user
