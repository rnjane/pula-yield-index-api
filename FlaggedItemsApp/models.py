from typing import Match
from django.db import models
from AuthenticationApp.models import User

# Create your models here.
class FlaggedItems(models.Model):
    flagged_item_reason = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)  