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
DEBUG_MODE = True


def print_debug_info(message):
    """Print message if DEBUG_MODE is True."""
    if DEBUG_MODE:
        print(f"DEBUG: {message}")


class Ecosystem():
    _test_mode = False
    _forced_choices = []

    def __init__(self, size, applicable_animals=None):
        self.size = size
        self.ecosystem_contents = [None] * size
        self.applicable_animals = applicable_animals or []
        self.statehistory = []
        self.populate_ecosystem()

    def populate_ecosystem(self):
        if not self.applicable_animals:
            print_debug_info(
                "No applicable animals to populate the ecosystem.")
            return
        else:
            for i in range(self.size):
                if self._test_mode is False:
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
        print_debug_info('behold, fluctuation!')
        for animal in self.ecosystem_contents:
            if animal is not None:
                animal.behave()

    def fill_empty_slots(self):
        for i in range(self.size):
            if self.ecosystem_contents[i] == []:
                self.ecosystem_contents[i] = None

    def set_contents_from_external(self, new_list):
        if len(self.ecosystem_contents) == len(new_list):
            self.statehistory.append(self.ecosystem_contents)
            self.ecosystem_contents = new_list
            self.fill_empty_slots()
        pass


class Animal(ABC):

    def __init__(self):
        self.id = id(self) % 10000

    @abstractmethod
    def behave(self):
        return self._instance_specific_move()

    def _instance_specific_move(self):
        """Instance-specific movement logic"""
        raise NotImplementedError("Subclasses must implement this method")

    def __repr__(self):
        return f"{self.__class__.__name__}#{self.id}"

    def __str__(self):
        return f"{self.__class__.__name__}#{self.id}"


class Bear(Animal):
    def _instance_specific_move(self):
        move = random.choice([-1, 0, 1])
        return move

    def behave(self):
        """Bear-specific behavior that uses the shared movement logic"""
        self.move_value = self._instance_specific_move()
        print_debug_info(self.move_value)
        # Could add bear-specific behavior here


class Fish(Animal):
    def _instance_specific_move(self):
        move = random.choice([-1, 0, 1])
        return move

    def behave(self):
        """Fish-specific behavior that uses the shared movement logic"""
        self.move_value = self._instance_specific_move()
        print_debug_info(self.move_value)
        # Could add fish-specific behavior here


class AnimalDispatcher():

    def __init__(self):
        self.queue = []
        self.slotted_queue = []

    def resolve_moves(self, ecosystem_instance):
        self.queue = ecosystem_instance.ecosystem_contents
        self.slotted_queue = [[] for _ in self.queue]
        # loop over original list and not touch it even
        for addr in range(len(self.queue)):
            if self.queue[addr] is not None:

                current_item = self.queue[addr]
                move = current_item.move_value

                # Calculate target index
                target_index = addr + move
                if target_index < 0:
                    target_index = 0
                if target_index >= len(self.queue):
                    target_index = len(self.queue)-1
                # Check if target index is valnot at corners
                # Add to target position (append to existing sublist)
                if len(self.slotted_queue[target_index]) == 0:
                    self.slotted_queue[target_index] = [current_item]
                else:
                    self.slotted_queue[target_index].append(current_item)

        print_debug_info(self.slotted_queue)
        return self.slotted_queue

    def process_collisions(self, ecosystem_instance):
        self.queue = ecosystem_instance.ecosystem_contents
        for slot in self.queue:
            if slot != None and len(slot) > 1:
                for animal in slot:
                    print_debug_info(f"Collision! {animal}")
        pass


Ecosystem._test_mode = True
# Force ecosystem population
Ecosystem._forced_choices = [Bear, Fish, Bear, Fish, None]


Volga = River(5)  # Size 6 to match mock lengths
# Check population (Bear, Fish, None, Bear, Fish, None)
print_debug_info(Volga)

flow = AnimalDispatcher()
Volga.fluctuate()

Volga.set_contents_from_external(flow.resolve_moves(Volga))
flow.process_collisions(Volga)
print_debug_info(Volga)
