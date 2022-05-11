import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Guinness Cake", 4.25, 2)

    def test_has_name(self):
        self.assertEqual("Guinness Cake", self.food.name)

    def test_has_price(self):
        self.assertEqual(4.25, self.food.price)

    def test_has_alcohol_level(self):
        self.assertEqual(2, self.food.rejuvination_level)