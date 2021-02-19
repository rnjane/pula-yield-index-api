from django.db import models
from AuthenticationApp.models import User

class Farmer(models.Model):
    name = models.CharField(max_length=30)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude  = models.DecimalField(max_digits=9, decimal_places=6)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='farmer_created_by', on_delete=models.CASCADE, default=None)
    modified_by = models.ForeignKey(User, related_name='farmer_updated_by', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name
