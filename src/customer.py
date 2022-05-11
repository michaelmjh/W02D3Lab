class Customer:

    def __init__(self, name, wallet, age, drunkeness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness = drunkeness

    def buy_drink(self, drink):
        self.decrease_wallet(drink)
        self.get_smashed(drink)
        

    def decrease_wallet(self, drink):
        self.wallet -= drink.price

    def get_smashed(self, drink):
        self.drunkeness += drink.alcohol_level

    def get_rejuvinated(self, food):
        self.drunkeness -= food.rejuvination_level