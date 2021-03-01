from django.db.models import Avg
from rest_framework.decorators import api_view
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import FlaggedItems
from .utils import find_outliers
from HarvestsApp.models import Harvest


def create_flagged_item(flagged_item_reason):
    item = FlaggedItems.objects.create(flagged_item_reason=flagged_item_reason)
    item.save()

@api_view()
def get_harvests_statistics(request):
    flagged_items = FlaggedItems.objects.all().values()
    harvest_records_count = Harvest.objects.count()
    average_wet_weight_yields = Harvest.objects.all().aggregate(Avg('harvest_wet_weight')).values()
    average_dry_weight_yields = Harvest.objects.all().aggregate(Avg('harvest_dry_weight')).values()
    number_of_flagged_items = FlaggedItems.objects.count()

    dry_weight_values = Harvest.objects.values_list('harvest_dry_weight', flat=True)
    wet_weight_values = Harvest.objects.values_list('harvest_wet_weight', flat=True)

    dry_weight_outliers = find_outliers(dry_weight_values)
    wet_weight_outliers = find_outliers(wet_weight_values)
    
    return Response({"dry_weight_outliers": dry_weight_outliers, "wet_weight_outliers": wet_weight_outliers,  "flagged_items": flagged_items, "harvest_records_count": harvest_records_count, "average_wet_weight_yields": average_wet_weight_yields, "average_dry_weight_yields": average_dry_weight_yields, "number_of_flagged_items": number_of_flagged_items })
