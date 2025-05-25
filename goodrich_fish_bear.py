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
    _test_mode = False
    _forced_choices = []

    def __init__(self, size):
        self.size = size
        self.contents = [None] * size
        self.applicable_animals = [Bear, Fish, None]
        self.populate()

    def recieve_contents(self, new_content):
        self.contents = new_content

    def populate(self):
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
                    self.contents[i] = tenant()
                else:
                    self.contents[i] = None

    def fill_empty_slots(self):
        for i in range(self.size):
            if self.contents[i] == []:
                self.contents[i] = None

    def __str__(self):
        return f"River  {self.size} and applicable animals: {self.applicable_animals} and contents like {self.contents}\n"


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
        self.slotted_queue = [[] for _ in self.queue]

    def trigger_moves(self):
        for item in self.queue:
            if item is not None and item._state == 1:
                item.move()
                item.set_state(0)

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
            cls._instance = super(Moves_dispatcher, cls).__new__(cls)
        return cls._instance

    def receive_contents(self, some_contents):
        self.queue = some_contents
        self.slotted_queue = [[] for _ in self.queue]

    def process_collisions(self, ecosystem_instance):
        self.queue = ecosystem_instance.ecosystem_contents
        for slot in self.queue:
            if slot != None and len(slot) > 1:
                animal_one = slot[0]
                animal_two = slot[1]
                animal_one.conflict(animal_two)
        pass

    def find_slot_for_child(self, ecosystem_instance):
        self.queue = ecosystem_instance.ecosystem_contents
        for index in range(len(self.queue)):
            if len(self.queue) == 0:
                return index

    def process_status(self, ecosystem_instance):
        pass


Volga = River(5)
Volga._forced_choices = [Bear, Fish, Bear, Fish, None]
print_debug_info(Volga)


md = Moves_dispatcher()

md.receive_contents(Volga.contents)
md.trigger_moves()
md.resolve_moves()

Volga.recieve_contents(md.return_contents())
print_debug_info(Volga)
