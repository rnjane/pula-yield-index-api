from django.db import models
from FarmsApp.models import Farm
from AuthenticationApp.models import User


class Harvest(models.Model):
    farm = models.ForeignKey(Farm, related_name='harvest', on_delete=models.CASCADE)
    harvest_wet_weight = models.FloatField()
    harvest_dry_weight = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='harvest_created_by', on_delete=models.CASCADE, default=None)
    modified_by = models.ForeignKey(User, related_name='harvest_updated_by', on_delete=models.CASCADE, default=None)

    @property
    def harvest_name(self):
        return self.farm.farm_name + " Harvest"


class HarvestPhotos(models.Model):
    belongs_to = models.ForeignKey(Harvest, related_name='harvest_photo', on_delete=models.CASCADE, default=None, null=True)
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='harvest_photo_created_by', on_delete=models.CASCADE, default=None)
    modified_by = models.ForeignKey(User, related_name='harvest_photo_updated_by', on_delete=models.CASCADE, default=None)
