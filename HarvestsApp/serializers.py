from django.db.models import fields
from rest_framework import serializers
from .models import Harvest, HarvestPhotos


class HarvestPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['belongs_to', 'image']


class HarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harvest
        fields = ['farm', 'harvest_wet_weight', 'harvest_dry_weight', 'date_created', 'date_updated', 'created_by', 'modified_by']
