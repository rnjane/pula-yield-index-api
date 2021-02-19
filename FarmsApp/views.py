  
from rest_framework import generics, permissions
from . import serializers, models


class FarmListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.FarmSerializer
    queryset = models.Farm.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class FarmGetEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.FarmSerializer
    queryset = models.Farm.objects.all()
