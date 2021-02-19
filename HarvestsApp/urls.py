from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    #harvest operations
    path('harvest', views.HarvestListCreateView.as_view(), name='list_create_harvest'),
    path('harvest-details/<str:pk>/', views.HarvestGetEditDeleteView.as_view(), name='get_edit_delete_harvest'),
    path('harvest-photo', views.HarvestPhotoListCreateView.as_view(), name='list_create_harvest_photo'),
    path('harvest-photo-details/<str:pk>/', views.HarvestPhotoGetEditDeleteView.as_view(), name='get_edit_delete_harvest_photo'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)