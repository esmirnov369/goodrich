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
    def __init__(self, size, applicable_animals=None):
        self.size = size
        self.ecosystem_contents = [None] * size
        self.applicable_animals = applicable_animals or []
        self.populate_ecosystem()



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
        return f"Ecosystem  {self.size} and applicable animals: {self.applicable_animals} and contents like {self.ecosystem_contents}\n"

class River(Ecosystem):
    def __init__(self, size):
        super().__init__(size, [Bear, Fish, None])  # Pass animals directly

    def fluctuate(self):
        print(f'behold, fluctuation!')
        for animal in self.ecosystem_contents:
            if animal != None: animal.behave()


class Animal(ABC):
    def __init__(self):
        self.id = id(self) % 10000

    @abstractmethod
    def behave(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}#{self.id}"  # Used in lists, debugging

    def __str__(self):
        return f"{self.__class__.__name__}#{self.id})"  # User-friendly print

class Bear(Animal):

    def behave(self):
        self.move_value = random.choice([0, 1, -1])

    def set_move(self, value):
        self.move_value = value


class Fish(Animal):

    def behave(self):
        self.move_value = random.choice([0, 1, -1])

    def set_move(self, value):
        self.move_value = value


class animal_dispatcher():

    def __init__(self, Ecosystem):
        self.queue = Ecosystem.ecosystem_contents
        self.slotted_queue = []

    def resolve_moves(self):
        self.slotted_queue =  [[] for _ in self.queue]
        #loop over original list and not touch it even
        for addr in range(len(self.queue)):
            if self.queue[addr] is not None:

                current_item = self.queue[addr]
                move = current_item.move_value

                # Calculate target index
                target_index = addr + move
                if target_index < 0: target_index = 0
                if target_index >= len(self.queue): target_index = len(self.queue)-1 
                # Check if target index is valnot at corners  
                # Add to target position (append to existing sublist)
                if len(self.slotted_queue[target_index]) == 0:
                    self.slotted_queue[target_index] = [current_item]
                else:
                    self.slotted_queue[target_index].append(current_item)
        
        print(self.slotted_queue)

    def process_collisions(self):
        pass


Volga = River(10)
print(Volga)
flow = animal_dispatcher(Volga)
Volga.fluctuate()
flow.resolve_moves()

