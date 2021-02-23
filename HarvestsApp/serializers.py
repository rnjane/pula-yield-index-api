from FarmsApp.models import Farm
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Harvest, HarvestPhotos


class HarvestPhotosSerializer(serializers.ModelSerializer):
    # image = serializers.ListField(
    #             child=serializers.FileField( max_length=100000,
    #                                      allow_empty_file=False,
    #                                     use_url=True ))
    class Meta:
        model = HarvestPhotos
        fields = ['belongs_to', 'image', 'date_created', 'date_updated', 'created_by', 'modified_by']
        extra_kwargs = {"created_by": {"read_only": True}, "modified_by": {"read_only": True}}

    # def create(self, validated_data):
    #     image=validated_data.pop('image')
    #     for img in image:
    #         photo=HarvestPhotos.objects.create(image=img,**validated_data)
    #     return photo


class HarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harvest
        fields = ['id', 'harvest_name', 'farm', 'harvest_wet_weight', 'harvest_dry_weight', 'date_created', 'date_updated', 'created_by', 'modified_by']
        extra_kwargs = {"created_by": {"read_only": True}, "modified_by": {"read_only": True}}
