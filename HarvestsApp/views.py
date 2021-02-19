from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, permissions
from . import serializers, models


class HarvestListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.HarvestSerializer
    queryset = models.Harvest.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, modified_by=self.request.user)


class HarvestGetEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.HarvestSerializer
    queryset = models.Harvest.objects.all()

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class HarvestPhotoListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.HarvestPhotosSerializer(many=True)
    queryset = models.HarvestPhotos.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, modified_by=self.request.user)


class HarvestPhotoGetEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.HarvestPhotosSerializer
    queryset = models.HarvestPhotos.objects.all()

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)
