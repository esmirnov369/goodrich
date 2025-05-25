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


class River():
    _test_mode = True if DEBUG_MODE is True else False

    def __init__(self, size):
        self._size = size
        self._contents = [None] * size
        self._applicable_animals = [Bear, Fish, None]
        self.populate()

    def receive_contents(self, new_content):
        self._contents = new_content

    def populate(self):
        if self._test_mode is True:
            self.forced_choices = [Bear, Fish, None, Fish, None]
        for i in range(self._size):
            if self._test_mode is False:
                tenant = random.choice(self._applicable_animals)
            else:
                tenant = self.forced_choices[i]
            if tenant is not None:
                # Instantiate the chosen animal class with a name
                self._contents[i] = tenant()
            else:
                self._contents[i] = None

    def fill_empty_slots(self):
        for i in range(self._size):
            if self._contents[i] == []:
                self._contents[i] = None

    def __str__(self):
        return (f"River size: {self._size}, "
                f"applicable animals: {self._applicable_animals}, "
                f"contents: {self._contents}\n")


class Animal(ABC):
    DEAD = -1
    NOMOVE = 0
    CANMOVE = 1

    def __init__(self, min_health=1, max_health=10, initial_state=CANMOVE):
        self.id = id(self) % 10000
        self._gender = random.choice(['male', 'female'])
        self._health = random.randint(min_health, max_health)
        self._state = initial_state
        self._move = 0

    def move(self):
        if self._state == self.CANMOVE:
            value = random.choice([-1, 0, 1])
            self._move = self.set_move(value)

    def set_move(self, value):
        self._move = value

    def set_state(self, state):
        if state == 0:
            self._state = self.NOMOVE
        elif state == 1:
            self._state = self.CANMOVE
        elif state == -1:
            self._state = self.DEAD

    def conflict(self, other_animal):
        product = self.mate(other_animal)
        if product is None:
            product = self.fight(other_animal)

    def mate(self, other_animal):
        if type(self) is type(other_animal):
            if self._gender != other_animal.gender:
                child = type(self)()
                child.set_state(1)
                self.set_state(1)
                other_animal.set_state(1)
                return child
            else:
                return None

    def fight(self, other_animal):
        if (type(self) is not type(other_animal)) or (self._gender == other_animal.gender):
            if self._state != 1 and other_animal.state != 1:
                if self._health > other_animal.health:
                    other_animal.set_state(self.DEAD)
                    self.set_state(self.NOMOVE)
                else:
                    other_animal.set_state(self.NOMOVE)
                    self.set_state(-1)
        return None

    def __repr__(self):
        return f"{self.__class__.__name__}#{self.id}"

    def __str__(self):
        return f"{self.__class__.__name__}#{self.id}"


class Bear(Animal):

    def __init__(self):
        super().__init__(min_health=10, max_health=15)


class Fish(Animal):

    def __init__(self):
        super().__init__(min_health=1, max_health=5)


class Moves_dispatcher():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Moves_dispatcher, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.queue = []
        self.slotted_queue = []

    def receive_contents(self, some_contents):
        self.queue = some_contents
        for item in self.queue:
            self.slotted_queue.append([item])

    def trigger_moves(self):
        for item in self.queue:
            if item is not None and item._state == item.CANMOVE:
                item.move()
                item.set_state(item.NOMOVE)

    def resolve_moves(self):
        for addr in range(len(self.queue)):
            if self.queue[addr] is not None:

                current_item = self.queue[addr]
                move = current_item._move
                current_item.set_move(0)

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

    def return_contents(self):
        return self.slotted_queue


class Conflict_Dispatcher():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Conflict_Dispatcher, cls).__new__(cls)
        return cls._instance

    def receive_contents(self, some_contents):
        self.slotted_queue = some_contents

    def process_collisions(self):
        for slot in self.slotted_queue:
            if slot is not None and len(slot) > 1:
                animal_one = slot[0]
                animal_two = slot[1]
                animal_one.conflict(animal_two)
        pass


class Queue_Cleaner():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Conflict_Dispatcher, cls).__new__(cls)
        return cls._instance


Volga = River(5)


print_debug_info(Volga)

md = Moves_dispatcher()

md.receive_contents(Volga._contents)
md.trigger_moves()
md.resolve_moves()

Volga.receive_contents(md.return_contents())
print_debug_info(Volga)
