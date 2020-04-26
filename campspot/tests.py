from django.test import TestCase
from campspot.models import campme

# Create your tests here.
class campspotTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    campspot model
    """

    def test_str(self):
        test_name = campme(name='A campspot')
        self.assertEqual(str(test_name), 'A campspot')