from django.test import TestCase
from .models import Utensil

# Create your tests here.
class UtensilTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product model
    """

    def test_str(self):
        test_name = Utensil(name='A utensil')
        self.assertEqual(str(test_name), 'A utensil')