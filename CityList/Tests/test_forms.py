import unittest

from django.test import TestCase
from ..forms import CityForm, LoginForm

class TestForms(TestCase):
    def test_city_form_valid_data(self):
        form = CityForm(data={
            'name': 'Test City',
            'website': 'http://www.testcity.com',
            'is_active': True,
            'state': 'NY'
        })

        self.assertTrue(form.is_valid())

    def test_login_form_no_data(self):
        form = LoginForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)  # There should be 2 errors for missing required fields


if __name__ == '__main__':
    unittest.main()
