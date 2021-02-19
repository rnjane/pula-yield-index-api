from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from model_mommy import mommy
from . import models
from FarmersApp.models import Farmer


class TestsSetUp(APITestCase):
    def setUp(self):
        self.admin_token = Token.objects.create(user=User.objects.create_superuser(username='testadminuser', email='testadmin@test.com'))
        self.admin_client = APIClient()
        self.admin_client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        self.test_farmer = mommy.make(Farmer)


class FarmsAppTests(TestsSetUp):
    '''tests related to categories'''
    def test_authenticated_user_can_add_a_farm(self):
        response = self.admin_client.post(reverse('list_create_farm'), {'farm_owner': self.test_farmer.id, 'farm_size': 12.23, 'crop_grown': 'Maize'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_authenticated_user_can_view_all_farms(self):
        response = self.admin_client.get(reverse('list_create_farm'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_farm_creatiom_requires_login(self):
        unauthorized_client = APIClient()
        response = unauthorized_client.post(reverse('list_create_farm'), {'farm_owner': self.test_farmer, 'farm_size': 12.23, 'crop_grown': 'Maize'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_aauthenticated_user_can_edit_a_farm_details(self):
        mommy.make(models.Farm)
        response = self.admin_client.patch(reverse('get_edit_delete_farm', kwargs={'pk': 1}), {'farm_size': 45.34})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(45.34, response.data['farm_size'])

    def test_authenticated_user_can_delete_a_farm(self):
        mommy.make(models.Farm)
        response = self.admin_client.delete(reverse('get_edit_delete_farm', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, None)