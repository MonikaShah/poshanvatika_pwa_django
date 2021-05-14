from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class UploadPictureModel(models.Model):
    picture = models.ImageField(upload_to='PoshanVatikaPics/', blank=True, null=True)
    name = models.CharField(max_length=30, default='')
    nutri_nm = models.CharField(max_length=100, default='')
    area = models.IntegerField()
    village = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    lat = models.CharField(max_length=10)
    lng = models.CharField(max_length=10)

class UploadWellPictureModel(models.Model):
    picture = models.ImageField(upload_to='WellPics/', blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    well_nm = models.CharField(max_length=100, blank=True, null=True)
    radius = models.IntegerField(blank=True, null=True)
    depth = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    village = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    lat = models.CharField(max_length=10)
    lng = models.CharField(max_length=10)

    
