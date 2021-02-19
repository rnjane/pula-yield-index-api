from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from model_mommy import mommy
from .models import Farmer


class TestsSetUp(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_user = mommy.make(User)
        self.token = Token.objects.create(user=self.test_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.test_farmer = mommy.make(Farmer, created_by=self.test_user, modified_by=self.test_user)


class FarmersAppTests(TestsSetUp):
    '''tests related to categories'''
    def test_authenticated_user_can_add_a_farmer(self):
        response = self.client.post(reverse('list_create_farmer'), {'name': 'testfarmer', 'longitude': 12.23, 'latitude': 34.55})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual('testfarmer', response.data['name'])

    def test_authenticated_user_can_view_all_farmers(self):
        response = self.client.get(reverse('list_create_farmer'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_farmer_creation_requires_login(self):
        unauthorized_client = APIClient()
        response = unauthorized_client.post(reverse('list_create_farmer'), {'name': 'testfarmer2', 'longitude': 12.23, 'latitude': 34.55})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_edit_a_farmer_details(self):
        response = self.client.patch(reverse('get_edit_delete_farmer', kwargs={'pk': 1}), {'name': 'new farmer name'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('new farmer name', response.data['name'])

    def test_authenticated_user_can_delete_a_farmer(self):
        response = self.client.delete(reverse('get_edit_delete_farmer', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, None)