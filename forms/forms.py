from django import forms 
from .models import BasicInformationModel,NutrigardenInformationModel


class BasicInformationForm(forms.ModelForm):
    class Meta:
        model = BasicInformationModel
        fields = ('organization','district','village','afifpartner','covervillage','averagehousehold','shg')


class NutrigardenInformationForm(forms.ModelForm):
    class Meta:
        model = NutrigardenInformationModel
        fields = ('village','pincode','nutrigardentype','size','use','varieties','backyard','unit','seed','nutrigardennumber','organic','training','afvillage','villagename','villagenumber','promote')
