from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=30)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude  = models.DecimalField(max_digits=9, decimal_places=6)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
