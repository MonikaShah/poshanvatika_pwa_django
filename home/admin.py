from django.contrib import admin

# Register your models here.

from .models import PoshanFormInformation, UploadPictureModel, UploadWellPictureModel
admin.site.register(UploadPictureModel)
admin.site.register(UploadWellPictureModel)
admin.site.register(PoshanFormInformation)