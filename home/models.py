from django.db import models

# Create your models here.

class PictureLocation(models.Model):
    picture_name = models.CharField(max_length=30)
    lat = models.CharField(max_length=10)
    lng = models.CharField(max_length=10)

    
