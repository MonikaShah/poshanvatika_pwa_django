from django.contrib import admin

# Register your models here.

from .models import UploadPictureModel, UploadWellPictureModel
admin.site.register(UploadPictureModel)
admin.site.register(UploadWellPictureModel)
