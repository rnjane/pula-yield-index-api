from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
from . import views

urlpatterns = [
    #Farm operations
    path('farm', views.FarmListCreateView.as_view(), name='list_create_farm'),
    path('farm-details/<str:pk>/', views.FarmGetEditDeleteView.as_view(), name='get_edit_delete_farm'),

    path('select-data', views.ReturnSelectData, name='select_data'),
]