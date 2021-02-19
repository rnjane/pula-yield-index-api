from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
from . import views

urlpatterns = [
    #Farmer operations
    path('farmer', views.FarmersListCreateView.as_view(), name='list_create_farmer'),
    path('farmer-details/<str:pk>/', views.FarmersGetEditDeleteView.as_view(), name='get_edit_delete_farmer'),
]