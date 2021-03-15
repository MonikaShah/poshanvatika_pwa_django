from django.forms import ModelForm
from .models import UploadPicture
from django import forms

class UploadPictureForm(ModelForm):
    picture = forms.ImageField(label='')
    area = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter Area Name','class': 'upload_field'}))
    village = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter village Name','class': 'upload_field'}))
    district = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter district Name','class': 'upload_field'}))
    state = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter state Name','class': 'upload_field'}))
    pincode = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter pincode','class': 'upload_field'}))
    class Meta:
            model = UploadPicture
            fields = '__all__'
