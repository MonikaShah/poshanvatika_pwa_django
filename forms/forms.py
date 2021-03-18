from django import forms 
from .models import BasicInformationModel,NutrigardenInformationModel, factsheetInformationModel, factsheetDynamicIndicatorsModel, financialExpensesModel

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
        model= factsheetInformationModel
        fields = ('location','state','district', 'ICDSProj', 'sector', 'village', 'anganwadi', 'famsize','typeofShed','patt','consump', 'typeOf')
        labels = {
            'location' : ('Location of Nutri-garden/ POSHAN Vatika'),
            'state' : ('State'),
            'district' : ('District'),
            'ICDSProj':('ICDS Project'),
            'sector' : ('Sector'),
            'village' : ('Village/Tola'),
            'anganwadi' : ('Anganwadi Centre'),
            'famsize' : ('If it is household (ICDS beneficiary) Nutri-garden then what is the family size of the household'),
            'typeofShed' : ('Type of vegetable/ fruit Nutri-garden shed'),
            'patt' : ('Nutri-garden patterns employed'),
            'consump': ('Consumption category of Nutri-garden'),
            'typeOf' : ('Type of Nutri-garden activity')
        }
        

class factsheetDynamicIndicatorsForm(forms.ModelForm):
    class Meta:
        model = factsheetDynamicIndicatorsModel
        fields = ('cultTech', 'seedtype', 'seedSource', 'seedbnkloc', 'fertType', 'fertSour', 'vermigrade', 'pest', 'fence', 'irrig', 'water', 'resrcLvrgd', 'govt', 'prov', 'provPlace')
        labels = {
            'cultTech' : ('Cultivation Technique'),
            'seedtype' : ('Type of Seed'),
            'seedSource' : ('Source of Seed'),
            'seedbnkloc' : ('If seed bank then location of seed bank'),
            'fertType' : ('Type of Fertilizer'),
            'fertSour' : ('Source of Fertilizer'),
            'vermigrade' : ('If vermicompost, then which grade'),
            'pest' : ('Pest Management'),
            'fence' : ('Type of Fences'),
            'irrig' : ('Irrigation method'),
            'water': ('Water source'),
            'resrcLvrgd' : ('Resources leveraged for the establishing the nutri-garden'),
            'govt' : ('If government scheme, then name it'),
            'prov' : ('Is there any provision for storage of produce'),
            'provPlace' : ('If Yes, then where')
        }


class financialExpensesForm(forms.ModelForm):
    class Meta:
        model = financialExpensesModel
        fields = ('soilPrep', 'fertilizers', 'seeds', 'cultTools', 'fence', 'transportation', 'labor', 'irrigation', 'miscellaneous')
        labels = {
            'soilPrep' : ('Soil preparation (including seeding bed)'),
            'fertilizers' : ('Fertilizers'),
            'seeds' : ('Seeds'),
            'cultTools' : ('Cultivation tools'),
            'fence' : ('Fence'),
            'transportation' : ('Transportation'),
            'labor' : ('Labor'),
            'irrigation' : ('Irrigation'),
            'miscellaneous': ('Miscellaneous')

        }


""" location = forms.CharField(label='Location of Nutri-garden/ POSHAN Vatika')
    state = forms.CharField(label='State')
    district = forms.CharField(label='District')
    ICDSProj = forms. CharField(label= 'ICDS Project')
    sector = forms.CharField(label='Sector')
    village = forms.CharField(label='Village/Tola')
    anganwadi = forms.CharField(label='Anganwadi Centre')"""
    
    
"""class factsheetInformationForm(forms.ModelForm):
    Location = forms.CharField(label='Location')
    State = forms.CharField(label='State')
    Famsize = forms.ChoiceField(label='Family size', widget=forms.Select(choices = CHOICES))
    class Meta:
        model = factsheetInformationModel
        fields='__all__'
        fields = ('location','state','district', 'ICDSProj', 'sector', 'village', 'anganwadi', 'famsize','typeofShed','pattern','consumption', 'typeOf', 'cultTech', 'seedtype', 'seedSource', 'seedbnkloc', 'fertType', 'fertSour', 'vermigrade', 'pest', 'fence', 'irrig', 'water', 'resrcLvrgd', 'govt', 'prov', 'provPlace')"""