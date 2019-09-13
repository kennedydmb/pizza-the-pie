from django.test import TestCase
from .models import Food_order

# Create your tests here.
class Food_orderTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product model
    """

    def test_str(self):
        test_name = Food_order(name='A food order')
        self.assertEqual(str(test_name), 'A food order')