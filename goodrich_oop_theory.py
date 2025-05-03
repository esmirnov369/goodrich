# critical life applications of software: rocket station, railway operator, retina surgery computer

# R-2.4 Write a Python class, Flower, that has three instance variables of type str,
# int, and float, that respectively represent the name of the flower, its number of petals, and its price. Your class must include a constructor method
# that initializes each variable to an appropriate value, and your class should
# include methods for setting the value of each type, and retrieving the value
# of each type


class Flower():
    def __init__(self, name, petals):
        self.name = name
        self.petals = petals

    def set_price(self, price):
        self.price = price

    def __repr__(self):
        return f'{self.name} with {self.petals} petals costs {self.price}'


flower123 = Flower('rose', 5)

flower123.set_price(69)

print(flower123)
