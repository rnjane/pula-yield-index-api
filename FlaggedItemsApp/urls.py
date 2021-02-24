from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('flagged-item', views.FlaggedItemListCreateView.as_view(), name='flagged_item'),
]