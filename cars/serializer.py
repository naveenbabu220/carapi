from rest_framework import serializers
from .models import Car

class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['make','color','production_year','avg_fuel_consumption_per_100km','max_passengers']
