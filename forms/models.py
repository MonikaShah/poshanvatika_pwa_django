from django.db import models
from django.conf import settings


nutrigardentype = [
            ('Organic', 'Organic'),
            ('Uses Chemical Fertilizer', 'Uses Chemical Fertilizer'),
           
]


class BasicInformationModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = 1)
    organization = models.CharField(max_length = 100)
    district  = models.CharField(max_length = 50)  
    village = models.CharField(max_length = 50)
    afifpartner = models.CharField(max_length = 10)
    afif = models.CharField(max_length=10,blank=True,null = True)
    covervillage = models.IntegerField()
    averagehousehold = models.IntegerField()
    shg = models.IntegerField()


class NutrigardenInformationModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = 1)
    village = models.CharField(max_length = 50)
    pincode = models.CharField(max_length = 6)
    nutrigardentype = models.CharField(max_length = 50)
    size = models.CharField(max_length = 50)
    use = models.CharField(max_length = 50)
    varieties  = models.CharField(max_length = 50)
    backyard = models.CharField(max_length = 10)
    unit = models.CharField(max_length = 10,blank=True,null = True)
    seed = models.CharField(max_length = 50)
    nutrigardennumber = models.IntegerField()
    organic = models.IntegerField()
    training = models.CharField(max_length  = 100)
    afvillage = models.CharField(max_length = 10,blank=True,null = True)
    villagename = models.CharField(max_length = 50,blank=True,null = True)
    villagenumber = models.CharField(max_length = 50,blank=True,null = True)
    promote = models.CharField(max_length = 10)


class factsheetInformationModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = 1)
    location = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    district = models.CharField(max_length = 50)
    ICDSProj = models.CharField(max_length = 50)
    sector = models.CharField(max_length = 50)
    village = models.CharField(max_length = 50)
    anganwadi = models.CharField(max_length = 50)
    famsize = models.CharField(max_length = 50,blank=True,null = True)
    typeofShed = models.CharField(max_length = 50,blank=True,null = True)
    pattern = models.CharField(max_length = 50,blank=True,null = True)
    consumption = models.CharField(max_length = 50,blank=True,null = True)
    typeOf = models.CharField(max_length = 50,blank=True,null = True)
    cultTech = models.CharField(max_length = 50,blank=True,null = True)
    seedtype = models.CharField(max_length = 50,blank=True,null = True)
    seedSource = models.CharField(max_length = 50,blank=True,null = True)
    seedbnkloc = models.CharField(max_length = 50,blank=True,null = True)
    fertType = models.CharField(max_length = 50,blank=True,null = True)
    fertSour = models.CharField(max_length = 50,blank=True,null = True)
    vermigrade = models.CharField(max_length = 50,blank=True,null = True)
    pest = models.CharField(max_length = 50,blank=True,null = True)
    fence = models.CharField(max_length = 50,blank=True,null = True)
    irrig = models.CharField(max_length = 50,blank=True,null = True)
    water = models.CharField(max_length = 50,blank=True,null = True)
    resrcLvrgd = models.CharField(max_length = 50,blank=True,null = True)
    govt = models.CharField(max_length = 50,blank=True,null = True)
    prov = models.CharField(max_length = 50,blank=True,null = True)
    provPlace = models.CharField(max_length = 50,blank=True,null = True)