from django.test import TestCase

# Create your tests here.

class TestTravis(Testcase):

    def test_travis_CI(self):
        self.assertEqual(2,2)