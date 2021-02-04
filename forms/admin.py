from django.contrib import admin

# Register your models here.


from .models import BasicInformationModel, NutrigardenInformationModel
admin.site.register(BasicInformationModel)
admin.site.register(NutrigardenInformationModel)