from django.db import models

# Create your models here.
class farm(models.Model):
    farm_num = models.CharField(max_length=255)
    farm_name = models.CharField(max_length=50)
    lat = models.CharField(max_length=255)
    long = models.CharField(max_length=255)
    distance = models.CharField(max_length=255)
    result = models.CharField(max_length=255)




