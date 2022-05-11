class Pub:

    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def sell_drink(self, drink, customer):
        if self.check_age(customer) and not self.check_if_smashed(customer):
            self.increase_till(drink.price)

    def check_age(self, customer):
        if customer.age >= 18:
            return True
        else:
            return False

    def check_if_smashed(self, customer):
        if customer.drunkeness >= 18:
            return True
        else:
            return False

    def increase_till(self, price):
        self.till += price

