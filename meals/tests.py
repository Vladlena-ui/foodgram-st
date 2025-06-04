from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):
    def test_str_representation(self):
        recipe = Recipe(title="Борщ")
        self.assertEqual(str(recipe), "Борщ")