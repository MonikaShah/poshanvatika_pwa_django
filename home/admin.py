from django.contrib import admin

# Register your models here.

from .models import PictureLocation, UploadPictureModel, UploadWellPictureModel, WellPictureLocationModel
admin.site.register(PictureLocation)
admin.site.register(UploadPictureModel)
admin.site.register(UploadWellPictureModel)
admin.site.register(WellPictureLocationModel)