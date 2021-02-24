from rest_framework import generics, permissions, status
from rest_framework.response import Response
from . import serializers, models


class FlaggedItemListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.FlaggedItemsSerializer
    queryset = models.FlaggedItems.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, modified_by=self.request.user)


def create_flagged_item(flagged_item_reason):
    item = models.FlaggedItems.objects.create(flagged_item_reason=flagged_item_reason)
    item.save()