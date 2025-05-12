import random
from abc import ABC, abstractmethod
# Write a Python program to simulate an ecosystem containing two types
# of creatures, bears and fish. The ecosystem consists of a river, which is
# modeled as a relatively large list. Each element of the list should be a
# Bear object, a Fish object, or None. In each time step, based on a random
# process, each animal either attempts to move into an adjacent list location
# or stay where it is. If two animals of the same type are about to collide in
# the same cell, then they stay where they are, but they create a new instance
# of that type of animal, which is placed in a random empty (i.e., previously
# None) location in the list. If a bear and a fish collide, however, then the
# fish dies (i.e., it disappears).


class Ecosystem():
    def __init__(self, size):
        self.size = size
        self.ecosystem_contents = [None] * size
        self.applicable_animals = []

    def populate_ecosystem(self):
        if not self.applicable_animals:
            print("No applicable animals to populate the ecosystem.")
            return
        else:
            for i in range(self.size):
                tenant = random.choice(self.applicable_animals)
                if tenant is not None:
                    # Instantiate the chosen animal class with a name
                    self.ecosystem_contents[i] = tenant()
                else:
                    self.ecosystem_contents[i] = None

    def __str__(self):
        return f"Ecosystem with size {self.size} and applicable animals: {self.applicable_animals} and contents like {self.ecosystem_contents}"


class River(Ecosystem):
    def __init__(self, size):
        super().__init__(size)  # Call the constructor of the superclass
        # Specify applicable animals for River
        self.applicable_animals = [Bear, Fish, None]

    def fluctuatate(self):
        for animal in self.ecosystem_contents:
            animal.behave()


class Animal(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def behave(self):
        pass


class Bear(Animal):

    def behave(self):
        self.move = random.choice([0, 1, -1])

    def set_move(self, value):
        self.move = value


class Fish(Animal):

    def behave(self):
        self.move = random.choice([0, 1, -1])

    def set_move(self, value):
        self.move = value


class animal_dispatcher(self, Ecosystem)


def __init__(self, Ecosystem):
    self.queue = Ecosystem.ecosystem_contents

    def resolve_movies(self):
        for item in self.queue:


Volga = River(10)
print(Volga)
Volga.populate_ecosystem()
flow = animal_dispatcher(Volga)

print(Volga)
