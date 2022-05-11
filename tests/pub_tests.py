import unittest
from src.pub import Pub
from src.drinks import Drink
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):


    def setUp(self):
        self.customer_1 = Customer("Josh", 10, 27, 0)
        self.customer_2 = Customer("Michael", 100, 17, 20)
        drink_1 = Drink("Guinness", 3.25, 5)
        drink_2 = Drink("Tenents", 3.50, 3)
        drinks = [drink_1, drink_2]           
        
        stock = {
           drink_1 : 5,
           drink_2 : 10
        }
        self.food = Food("Guinness Cake", 4.25, 2)
        self.pub = Pub("Hello", 1000.00, drinks)
        
stock.key().name
    def test_has_name(self):
        self.assertEqual("Hello", self.pub.name)

    def test_has_cash(self):
        self.assertEqual(1000.00, self.pub.till)

    def test_has_drinks(self):
        self.assertEqual(2, len(self.pub.drinks))

    def test_sell_drink(self):
        self.pub.sell_drink(self.pub.drinks[0], self.customer_1)
        self.assertEqual(1003.25, self.pub.till)

    def test_check_age_pass(self):
        old_enough_to_drink = self.pub.check_age(self.customer_1)
        self.assertEqual(True, old_enough_to_drink)

    def test_check_age_fail(self):
        old_enough_to_drink = self.pub.check_age(self.customer_2)
        self.assertEqual(False, old_enough_to_drink)
        
    def test_check_drunkeness_pass(self):
        is_smashed = self.pub.check_if_smashed(self.customer_1)
        self.assertEqual(False, is_smashed)

    def test_check_drunkeness_fail(self):
        is_smashed = self.pub.check_if_smashed(self.customer_2)
        self.assertEqual(True, is_smashed)