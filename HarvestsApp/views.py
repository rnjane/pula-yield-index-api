from rest_framework import generics, permissions, status
from rest_framework.response import Response
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
    serializer_class = serializers.HarvestPhotosSerializer
    queryset = models.HarvestPhotos.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = serializers.HarvestPhotosSerializer(queryset, many=True)
        return Response(serializer.data)


class HarvestPhotoGetEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.HarvestPhotosSerializer
    queryset = models.HarvestPhotos.objects.all()

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)