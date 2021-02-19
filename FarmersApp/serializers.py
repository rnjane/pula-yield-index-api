from rest_framework import serializers
from . import models


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Farmer
        fields = ['name', 'latitude', 'longitude', 'date_created', 'date_updated', 'created_by', 'modified_by']
        extra_kwargs = {"created_by": {"read_only": True}, "modified_by": {"read_only": True}}
