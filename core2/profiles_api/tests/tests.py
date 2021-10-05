from django.test import TestCase
from profiles_api.models import UserProfile

class AnimalTestCase(TestCase):
    def setUp(self):
        UserProfile.objects.create(email="lion@gmail.com", name="roar", password="")
        UserProfile.objects.create(email="cat@gmail.com", name="meow", password="")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = UserProfile.objects.get(email="lion@gmail.com")
        cat = UserProfile.objects.get(email="cat@gmail.com")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
