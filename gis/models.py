from django.db import models

# Create your models here.
class Farm(models.Model):
    farm_num = models.CharField(max_length=150)
    farm_name = models.CharField(max_length=150)
    lat = models.CharField(max_length=150)
    long = models.CharField(max_length=300)
    distance = models.CharField(max_length=150)
    result = models.CharField(max_length=150)




