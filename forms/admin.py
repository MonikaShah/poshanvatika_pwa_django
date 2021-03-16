from django.contrib import admin

# Register your models here.


from .models import BasicInformationModel, NutrigardenInformationModel, factsheetInformationModel
admin.site.register(BasicInformationModel)
admin.site.register(NutrigardenInformationModel)
admin.site.register(factsheetInformationModel)