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

    # def post(self, request, format=None):
    #     data = request.data
    #     if isinstance(data, list):  # <- is the main logic
    #         serializer = self.get_serializer(data=self.request.data.lists()['image'], many=True)
    #     else:
    #         serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(created_by=self.request.user, modified_by=self.request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def perform_create(self, serializer, *args ):
    #     print("*********")
    #     # images = json.loads(self.request.data)
    #     for image in dict(self.request.data.lists())['image']:
    #         serializer.save(image=image, created_by=self.request.user, modified_by=self.request.user)


class HarvestPhotoGetEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.HarvestPhotosSerializer
    queryset = models.HarvestPhotos.objects.all()

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)