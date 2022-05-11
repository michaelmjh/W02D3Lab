import unittest
from src.drinks import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Guinness", 3.25, 5)

    def test_has_name(self):
        self.assertEqual("Guinness", self.drink.name)

    def test_has_price(self):
        self.assertEqual(3.25, self.drink.price)

    def test_has_alcohol_level(self):
        self.assertEqual(5, self.drink.alcohol_level)