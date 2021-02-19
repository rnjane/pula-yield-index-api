from FarmsApp.models import Farm
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Harvest, HarvestPhotos


class HarvestPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HarvestPhotos
        fields = ['belongs_to', 'image', 'date_created', 'date_updated', 'created_by', 'modified_by']
        extra_kwargs = {"created_by": {"read_only": True}, "modified_by": {"read_only": True}}


class HarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harvest
        fields = ['farm', 'harvest_wet_weight', 'harvest_dry_weight', 'date_created', 'date_updated', 'created_by', 'modified_by']
        extra_kwargs = {"created_by": {"read_only": True}, "modified_by": {"read_only": True}}
