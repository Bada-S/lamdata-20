"""Create a class to practice OOP"""


class Beverage:
    """drink class"""
    def __init__(self, name, price, iced, alcoholic):
        self.name = str(name)
        self.price = float(price)
        self.iced = bool(iced)
        self.alcoholic = bool(alcoholic)

    def drink(self):
        print("Sip sip")
