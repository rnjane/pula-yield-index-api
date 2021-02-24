from django.urls import reverse
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Harvest, HarvestPhotos

from FlaggedItemsApp.views import create_flagged_item


class HarvestPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HarvestPhotos
        fields = '__all__'
        extra_kwargs = {"created_by": {"read_only": True}, "modified_by": {"read_only": True}, "image_name": {"read_only": True}}

    
    def create(self, validated_data):
        images_data = self.context.get('request').data.pop('image')
        if len(images_data) < 3:
            create_flagged_item("There are less than 3 photos for this harvest")

        for image_data in images_data:
            if HarvestPhotos.objects.filter(image_name=image_data).exists():
                create_flagged_item("image already in use")
            image, _ = HarvestPhotos.objects.get_or_create(image=image_data, image_name=image_data, created_by=self.context.get('request').user, modified_by=self.context.get('request').user)

        return image


class HarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harvest
        fields = ['id', 'harvest_name', 'farm', 'harvest_wet_weight', 'harvest_dry_weight', 'date_created', 'date_updated', 'created_by', 'modified_by']
        extra_kwargs = {"created_by": {"read_only": True}, "modified_by": {"read_only": True}}

    def create(self, validated_data):
        harvests = Harvest.objects.filter(farm=validated_data.get('farm')).all()
        if len(harvests) > 0:
            create_flagged_item("Farm has more than one harvest")
        harvest = Harvest.objects.create(**validated_data)
        return harvest