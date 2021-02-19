from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from model_mommy import mommy
from . import models


class TestsSetUp(APITestCase):
    def setUp(self):
        self.admin_token = Token.objects.create(user=User.objects.create_superuser(username='testadminuser', email='testadmin@test.com'))
        self.admin_client = APIClient()
        self.admin_client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)


class FarmersAppTests(TestsSetUp):
    '''tests related to categories'''
    def test_authenticated_user_can_add_a_farmer(self):
        response = self.admin_client.post(reverse('list_create_farmer'), {'name': 'testfarmer', 'longitude': 12.23, 'latitude': 34.55})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual('testfarmer', response.data['name'])
    
    def test_authenticated_user_can_view_all_farmers(self):
        response = self.admin_client.get(reverse('list_create_farmer'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_farmer_creatiom_requires_login(self):
        unauthorized_client = APIClient()
        response = unauthorized_client.post(reverse('list_create_farmer'), {'name': 'testfarmer2', 'longitude': 12.23, 'latitude': 34.55})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_edit_a_farmer_details(self):
        mommy.make(models.Farmer, name='testfarmer2')
        response = self.admin_client.patch(reverse('get_edit_delete_farmer', kwargs={'pk': 1}), {'name': 'new farmer name'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('new farmer name', response.data['name'])

    def test_authenticated_user_can_delete_a_farmer(self):
        mommy.make(models.Farmer)
        response = self.admin_client.delete(reverse('get_edit_delete_farmer', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, None)