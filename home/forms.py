from django.forms import ModelForm
from .models import UploadPicture
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


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
