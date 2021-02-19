from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class TestsSetUp(APITestCase):
    def setUp(self):
        self.client = APIClient()
        User.objects.create_user(username='testuser', email='test@test.com', password='testpass12')
        self.user = User.objects.get(username='testuser')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.admin_token = Token.objects.create(user=User.objects.create_superuser(username='testadminuser', email='testadmin@test.com'))
        self.admin_client = APIClient()
        self.admin_client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)


class UserAuthTests(TestsSetUp):
    '''Authentication related tests'''
    def test_user_login_successful_with_valid_credentials(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass12'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_login_with_wrong_credentials_fail(self):
        response = self.client.post(reverse('login'), {'username': 'wrongusername', 'password': 'wrongone'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_login_with_missing_credentials_fail(self):
        response = self.client.post(reverse('login'), {'password': 'wrongone'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_only_admin_can_create_a_new_user(self):
        response = self.client.post(reverse('register'), {'username': 'test_user', 'email': 'test2@test.com', 'password': 'testpass'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn('You do not have permission to perform this action.', response.data['detail'])

    def test_admin_user_register_succeeds(self):
        response = self.admin_client.post(reverse('register'), {'username': 'test_user', 'email': 'test3@test.com', 'password': 'testPass12'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
