from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

class PictureLocation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    picture_name = models.CharField(max_length=30)
    lat = models.CharField(max_length=10)
    lng = models.CharField(max_length=10)

    
