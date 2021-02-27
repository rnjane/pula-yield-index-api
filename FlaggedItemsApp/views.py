from django.db.models import Avg
from rest_framework.decorators import api_view
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from . import serializers, models
from HarvestsApp.models import Harvest


def create_flagged_item(flagged_item_reason):
    item = models.FlaggedItems.objects.create(flagged_item_reason=flagged_item_reason)
    item.save()

@api_view()
def get_harvests_statistics(request):
    flagged_items = models.FlaggedItems.objects.all().values()
    harvest_records_count = Harvest.objects.count()
    average_wet_weight_yields = Harvest.objects.all().aggregate(Avg('harvest_wet_weight')).values()
    average_dry_weight_yields = Harvest.objects.all().aggregate(Avg('harvest_dry_weight')).values()
    number_of_flagged_items = models.FlaggedItems.objects.count()
    return Response({"flagged_items": flagged_items, "harvest_records_count": harvest_records_count, "average_wet_weight_yields": average_wet_weight_yields, "average_dry_weight_yields": average_dry_weight_yields, "number_of_flagged_items": number_of_flagged_items })
