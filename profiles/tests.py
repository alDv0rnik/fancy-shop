import pytest

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class TestProfile(TestCase):

    @pytest.mark.django_db
    def setUp(self) -> None:
        self.client = Client()
        self.credentials = {
            "username": "test_user",
            "password": "t954_yIO8!"
        }
        self.user = User.objects.create_user(self.credentials)

    def test_authentication(self):
        self.client.force_login(self.user)
        response = self.client.get("/register")
        self.assertEqual(response.status_code, 301)

    def test_register_url(self):
        self.client.logout()
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_view(self):
        self.client.force_login(self.user)
        url = reverse("profile_details", kwargs={"profile_slug": "test-user"})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)