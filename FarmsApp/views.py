  
from django.views.generic.base import View
from django.http import JsonResponse
from rest_framework import generics, permissions
from . import serializers, models


class FarmListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.FarmSerializer
    queryset = models.Farm.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, modified_by=self.request.user)


class FarmGetEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.FarmSerializer
    queryset = models.Farm.objects.all()

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


def ReturnSelectData(View):
    crops_grown = [crop[0] for crop in models.crops_grown]
    farm_size_units = [size[0] for size in models.farm_size_units]
    return JsonResponse({"crops_grown": crops_grown, "farm_size_units": farm_size_units})