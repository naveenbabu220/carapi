from django.db import models
from django.utils.text import slugify 
import uuid

# Create your models here.
class Car(models.Model):
    id = models.AutoField(primary_key= True,auto_created=True)
    make = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    production_year = models.IntegerField()
    avg_fuel_consumption_per_100km = models.FloatField()
    uuid= models.UUIDField(default=uuid.uuid4)
    max_passengers = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    
