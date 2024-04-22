import pytest

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class ProfileTest(TestCase):

    @pytest.mark.django_db
    def setUp(self):
        self.client = Client()
        self.credentials = {"username": "test_user", "password": "t49q3;uGU"}
        self.user = User.objects.create_user(self.credentials)
        self.slug = "sport"

    def test_view(self):
        url = reverse('profile_details', kwargs={"profile_slug": "test-user"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_authentication(self):
        self.client.force_login(self.user)
        response = self.client.get('/register')
        assert response.status_code == 301 or response.status_code == 302

