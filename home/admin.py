from django.contrib import admin

# Register your models here.

from .models import PictureLocation, UploadPicture
admin.site.register(PictureLocation)
admin.site.register(UploadPicture)
