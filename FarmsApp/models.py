from django.db import models
from FarmersApp.models import Farmer


farm_size_units = ( 
    ("Acres", "Acres"), 
    ("Hectares", "Hectares"), 
    ("Meter Squared", "Meter Squared"),
) 
class Farm(models.Model):
    farm_owner = models.ForeignKey(Farmer, related_name='farm', on_delete=models.CASCADE)
    farm_size = models.FloatField()
    farm_size_units = models.CharField(max_length=20, choices=farm_size_units, default="Acres")
    crop_grown = models.CharField(max_length=40)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.farm_owner + "'s" + self.crop_grown + "farm"
