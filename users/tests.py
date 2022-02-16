import profile
from django.test import TestCase
from django.urls import  reverse
from .models import Profile
from .views import profile




class RoomInspectorTest(TestCase):
    def test_profile_list_response(self):
        url = reverse("users:profile_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        
    def test_user_name_response(self):
        url = reverse("users:user_name", args=(profile.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  