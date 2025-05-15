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
    _test_mode = False
    _forced_choices = []
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
                if self._test_mode == False:
                    tenant = random.choice(self.applicable_animals)
                else:
                    tenant = self._forced_choices[i]    
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
    _test_mode = False
    _forced_move = None
    
    def __init__(self):
        self.id = id(self) % 10000
        self.move_value = 0  # Initialize move value

    @abstractmethod
    def behave(self):
        """Child classes must implement this, but can use self._determine_move()"""
        pass
        
    def _determine_move(self):
        """Encapsulated movement logic that all animals can reuse"""
        if self._test_mode and self._forced_move is not None:
            return self._forced_move
        return random.choice([-1, 0, 1])

    def set_move(self, value):
        """Optional setter if you need explicit control"""
        self.move_value = value

    def __repr__(self):
        return f"{self.__class__.__name__}#{self.id}"

    def __str__(self):
        return f"{self.__class__.__name__}#{self.id}"


class Bear(Animal):
    def behave(self):
        """Bear-specific behavior that uses the shared movement logic"""
        self.move_value = self._determine_move()
        # Could add bear-specific behavior here


class Fish(Animal):
    def behave(self):
        """Fish-specific behavior that uses the shared movement logic"""
        self.move_value = self._determine_move()
        # Could add fish-specific behavior here


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

Ecosystem._test_mode = True
Ecosystem._forced_choices = [Bear, Fish, None]  # Force ecosystem population
Animal._test_mode = True



Volga = River(3)  # Size 6 to match mock lengths
print(Volga)  # Check population (Bear, Fish, None, Bear, Fish, None)

flow = animal_dispatcher(Volga)
Volga.fluctuate()  # Calls behave(), which now uses mocked moves [1, -1, 0, 1, -1, 0]
flow.resolve_moves()  # Process collisions based on mocked moves


