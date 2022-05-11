import unittest
from src.customer import Customer
from src.drinks import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer_1 = Customer("Josh", 10, 27, 0)
        self.customer_2 = Customer("Michael", 100, 17, 20)
        self.drink = Drink("Ginness", 3.25, 5)
        self.food = Food("Guinness Cake", 4.25, 2)

    def test_has_name(self):
        self.assertEqual("Josh", self.customer_1.name)

    def test_has_cash(self):
        self.assertEqual(10, self.customer_1.wallet)

    def test_has_age(self):
        self.assertEqual(27, self.customer_1.age)

    def test_buy_drink(self):
        self.customer_1.buy_drink(self.drink)
        self.assertEqual(6.75, self.customer_1.wallet)

    def test_has_drunkeness(self):
        self.assertEqual(0, self.customer_1.drunkeness)

    def test_increase_drunkeness(self):
        self.customer_1.get_smashed(self.drink)
        self.assertEqual(5, self.customer_1.drunkeness)

    def test_reduce_drunkeness(self):
        self.customer_2.get_rejuvinated(self.food)
        self.assertEqual(18, self.customer_2.drunkeness)