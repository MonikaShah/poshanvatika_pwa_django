from django.db import models


nutrigardentype = [
            ('Organic', 'Organic'),
            ('Uses Chemical Fertilizer', 'Uses Chemical Fertilizer'),
           
]


class BasicInformationModel(models.Model):
    organization = models.CharField(max_length = 100)
    district  = models.CharField(max_length = 50)  
    village = models.CharField(max_length = 50)
    afifpartner = models.CharField(max_length = 10)
    afif = models.CharField(max_length=10,blank=True,null = True)
    covervillage = models.IntegerField()
    averagehousehold = models.IntegerField()
    shg = models.IntegerField()


class NutrigardenInformationModel(models.Model):
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


