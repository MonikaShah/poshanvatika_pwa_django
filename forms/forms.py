from django import forms 
from .models import BasicInformationModel,NutrigardenInformationModel, factsheetInformationModel


class BasicInformationForm(forms.ModelForm):
    class Meta:
        model = BasicInformationModel
        fields = ('organization','district','village','afifpartner','covervillage','averagehousehold','shg')


class NutrigardenInformationForm(forms.ModelForm):
    class Meta:
        model = NutrigardenInformationModel
        fields = ('village','pincode','nutrigardentype','size','use','varieties','backyard','unit','seed','nutrigardennumber','organic','training','afvillage','villagename','villagenumber','promote')

class factsheetInformationForm(forms.ModelForm):
    class Meta:
        model = factsheetInformationModel
        fields = ('location','state','district', 'ICDSProj', 'sector', 'village', 'anganwadi', 'famsize','typeofShed','pattern','consumption', 'typeOf', 'cultTech', 'seedtype', 'seedSource', 'seedbnkloc', 'fertType', 'fertSour', 'vermigrade', 'pest', 'fence', 'irrig', 'water', 'resrcLvrgd', 'govt', 'prov', 'provPlace')
        