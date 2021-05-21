from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from django.db.models.fields.files import ImageField
from django.core.exceptions import ValidationError
import easygui


# Create your models here.

def validate_image(image):
    file_size = image.file.size
    limit_mb = 15
    if file_size > limit_mb * 1024 * 1024:
        easygui.msgbox("Upload image lesser than 15 MB", title="Warning!")
        raise ValidationError("Max size of file is %s MB" % limit_mb)

class UploadPictureModel(models.Model):
    picture = models.ImageField(upload_to='PoshanVatikaPics/', blank=True, null=True, validators=[validate_image])
    name = models.CharField(max_length=100, default='')
    nutri_nm = models.CharField(max_length=100, default='')
    area = models.IntegerField()
    village = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=8, blank=True, null=True)
    lat = models.CharField(max_length=15)
    lng = models.CharField(max_length=15)

class UploadWellPictureModel(models.Model):
    picture = models.ImageField( upload_to='WellPics/', blank=True, null=True, validators=[validate_image])
    name = models.CharField(max_length=100, blank=True, null=True)
    well_nm = models.CharField(max_length=100, blank=True, null=True)
    radius = models.IntegerField(blank=True, null=True)
    depth = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    village = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=8, blank=True, null=True)
    lat = models.CharField(max_length=15)
    lng = models.CharField(max_length=15)
