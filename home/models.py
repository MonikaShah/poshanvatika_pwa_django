from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

class PictureLocation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    picture_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30, default='')
    nutrinm = models.CharField(max_length=100, default='')
    lat = models.CharField(max_length=10)
    lng = models.CharField(max_length=10)

class UploadPictureModel(models.Model):
    picture = models.FileField(upload_to='uploadPics/', blank=True, null=True)
    name = models.CharField(max_length=30, default='')
    nutri_nm = models.CharField(max_length=100, default='')
    area = models.CharField(max_length=30)
    village = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.CharField(max_length=10)

class WellPictureLocation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    picture_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    wellnm = models.CharField(max_length=100)
    radius = models.IntegerField()
    depth = models.IntegerField()
    level = models.IntegerField()
    lat = models.CharField(max_length=10)
    lng = models.CharField(max_length=10)

class UploadWellPictureModel(models.Model):
    picture = models.FileField(upload_to='uploadPics/', blank=True, null=True)
    name = models.CharField(max_length=30)
    well_nm = models.CharField(max_length=100)
    radius = models.IntegerField()
    depth = models.IntegerField()
    level = models.IntegerField()
    village = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.CharField(max_length=10)
    
