from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from model_mommy import mommy
import tempfile
from PIL import Image

from . import models
from HarvestsApp.models import Harvest, HarvestPhotos
from FarmsApp.models import Farm
from FarmersApp.models import Farmer

class TestsSetUp(APITestCase):
    def get_temporary_image(self):
        '''create a temporary image for testing purposes'''
        image = Image.new('RGB', (200, 200))
        temporary_image = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(temporary_image, 'jpeg')
        temporary_image.seek(0)
        return temporary_image

    def setUp(self):
        self.client = APIClient()
        self.test_user = mommy.make(User)
        self.token = Token.objects.create(user=self.test_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.test_user = mommy.make(User)
        self.test_farmer = mommy.make(Farmer, created_by=self.test_user, modified_by=self.test_user)
        self.test_farm = mommy.make(Farm, farm_owner=self.test_farmer, created_by=self.test_user, modified_by=self.test_user)
        self.test_harvest = mommy.make(Harvest, farm=self.test_farm, created_by=self.test_user, modified_by=self.test_user)

class HarvestsAppTests(TestsSetUp):
    def test_authenticated_user_can_add_a_harvest(self):
        response = self.client.post(reverse('list_create_harvest'), {'farm': self.test_farmer.id, 'harvest_wet_weight': 12.23, 'harvest_dry_weight': 9.23})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_authenticated_user_can_view_all_harvests(self):
        response = self.client.get(reverse('list_create_harvest'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_harvest_creation_requires_login(self):
        unauthorized_client = APIClient()
        response = unauthorized_client.post(reverse('list_create_harvest'), {'farm': self.test_farmer.id, 'harvest_wet_weight': 12.23, 'harvest_dry_weight': 9.23})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_edit_a_harvest_details(self):
        response = self.client.patch(reverse('get_edit_delete_harvest', kwargs={'pk': 1}), {'harvest_wet_weight': 45.34})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(45.34, response.data['harvest_wet_weight'])

    def test_authenticated_user_can_delete_a_harvest(self):
        response = self.client.delete(reverse('get_edit_delete_harvest', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, None)