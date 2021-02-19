from rest_framework import serializers
from . import models


class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Farm
        fields = ['farm_owner', 'farm_size', 'farm_size_units', 'crop_grown', 'date_created', 'date_updated', 'created_by', 'modified_by']
        extra_kwargs = {"created_by": {"read_only": True}, "modified_by": {"read_only": True}}
