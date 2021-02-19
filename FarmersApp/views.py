  
from rest_framework import generics, permissions
from . import serializers, models


class FarmersListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.FarmerSerializer
    queryset = models.Farmer.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class FarmersGetEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.FarmerSerializer
    queryset = models.Farmer.objects.all()
