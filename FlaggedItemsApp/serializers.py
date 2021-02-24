from FarmsApp.models import Farm
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import FlaggedItems


class FlaggedItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlaggedItems
        fields = '__all__'
        extra_kwargs = {"created_by": {"read_only": True}, "modified_by": {"read_only": True}}
