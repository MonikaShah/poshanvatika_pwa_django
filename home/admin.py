from django.contrib import admin

# Register your models here.

from .models import PictureLocation, UploadPictureModel, UploadWellPictureModel, WellPictureLocation
admin.site.register(PictureLocation)
admin.site.register(UploadPictureModel)
admin.site.register(UploadWellPictureModel)
