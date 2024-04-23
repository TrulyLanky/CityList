import unittest
from django.test import TestCase
from django.urls import reverse
from ..models import City
from django.contrib.auth.models import User


class CityModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for testing
        cls.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

        # Set up non-modified objects used by all test methods
        City.objects.create(name='Test City', is_active=True, website='http://www.testcity.com', state='NY', user=cls.user)

    def test_name_content(self):
        city = City.objects.get(id=1)
        expected_object_name = f'{city.name}'
        self.assertEqual(expected_object_name, 'Test City')

    def test_is_active_content(self):
        city = City.objects.get(id=1)
        self.assertTrue(city.is_active)

    def test_website_content(self):
        city = City.objects.get(id=1)
        expected_website = f'{city.website}'
        self.assertEqual(expected_website, 'http://www.testcity.com')

    def test_state_content(self):
        city = City.objects.get(id=1)
        expected_state = f'{city.state}'
        self.assertEqual(expected_state, 'NY')

    def test_user_relation(self):
        city = City.objects.get(id=1)
        self.assertEqual(city.user.username, 'testuser')

    def test_get_absolute_url(self):
        city = City.objects.get(id=1)
        expected_url = reverse('city-details', args=[str(city.pk)])
        self.assertEqual(city.get_absolute_url(), expected_url)


if __name__ == '__main__':
    unittest.main()
