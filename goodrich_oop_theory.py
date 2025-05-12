import random
import string

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

# Use the techniques of Section 1.7 to revise the charge and make payment
# methods of the CreditCard class to ensure that the caller sends a number
# as a parameter

# R-2.6 If the parameter to the make payment method of the CreditCard class
# were a negative number, that would have the effect of raising the balance
# on the account. Revise the implementation so that it raises a ValueError if
# a negative value is sent.

# R-2.7 The CreditCard class of Section 2.3 initializes the balance of a new account to zero. Modify that class so that a new account can be given a
# nonzero balance using an optional fifth parameter to the constructor. The
# four-parameter constructor syntax should continue to produce an account
# with zero balance.

# R-2.8 Modify the declaration of the first for loop in the CreditCard tests, from
# Code Fragment 2.3, so that it will eventually cause exactly one of the three
# credit cards to go over its credit limit. Which credit card is it?


class CreditCard:
    """A consumer credit card."""

    def __init__(
        self,
        customer: str,
        bank: str,
        account: str,
        limit: float,
        optionalBalance: int | None = 0  # Optional (explicit None type)
    ):
        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = limit
        self.balance = 0 + optionalBalance

    def get_customer(self):
        """Return name of the customer."""
        return self.customer

    def get_bank(self):
        """Return the bank's name."""
        return self.bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self.account

    def get_limit(self):
        """Return current credit limit."""
        return self.limit

    def get_balance(self):
        """Return current balance."""
        return self.balance

    def charge(self, price):

        try:
            assert price > 0, "val should be positive"
            """Charge given price to the card, assuming sufficient credit limit.

            Return True if charge was processed; False if charge was denied.
            """
            if price + self.balance > self.limit:  # if charge would exceed limit,
                return False  # cannot accept charge
            else:
                self.balance += price
                return True
        except TypeError:
            raise TypeError

    def make_payment(self, amount):
        try:
            assert amount > 0, 'amount cannot be negative'
            self.balance -= amount
        except TypeError:
            raise TypeError


class PredatoryCreditCard(CreditCard):
    def __init__(self, customer: str, bank: str, acnt: str, limit: float,
                 apr: float, balance: int | None = 0):
        """Create a new predatory credit card instance.

        Args:
            customer: Name of the customer
            bank: Name of the bank
            acnt: Account identifier
            limit: Credit limit (in dollars)
            apr: Annual percentage rate (e.g., 0.0825 for 8.25% APR)
            balance: Optional starting balance (defaults to 0)
        """
        super().__init__(customer, bank, acnt, limit, balance)
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        """
        success = super().charge(price)  # call inherited method
        if not success:
            self.balance += 5  # assess penalty
        return success  # caller expects return value

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self.balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self.balance *= monthly_factor


class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, data):
        if isinstance(data, int):
            if data < 0:
                raise ValueError("Dimension must be non-negative")
            self.coords = [0.0] * data  # Create a list of zeros
        elif isinstance(data, (list, tuple)):  # Accepts lists or tuples
            if not all(isinstance(x, (int, float)) for x in data):
                raise TypeError("All elements must be numbers (int/float)")
            self.coords = [float(x) for x in data]  # Convert all to float
        else:
            raise TypeError("Input must be an int or a list/tuple of numbers")

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self.coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self.coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self.coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __radd__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __mul__(self, multiplier):
        if isinstance(multiplier, int):
            result = Vector(len(self))  # start with vector of zeros
            for j in range(len(self)):
                result[j] = self[j] * multiplier
            return result
        elif isinstance(multiplier, Vector) and len(multiplier) == len(self):
            result = 0
            for j in range(len(self)):
                result = result + self[j] * multiplier[j]
            return result
        else:
            raise TypeError("Multiplier must be either int or Vector")

    def __rmul__(self, multiplier):
        """Handle scalar * vector (delegates to __mul__)."""
        return self * multiplier  # Reuse __mul__ logic

    def __sub__(self, other):
        """Return diff  of two vectors."""
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        """Return neg of a vectors."""
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * -1
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self.coords == other.coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other  # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self.coords)[1:-1] + '>'  # adapt list representation


if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard('John Smith', 'California Savings',
                             '5391 0375 9387 5309', 2500))
    wallet.append(CreditCard('MIke Bowman', 'California Federal',
                             '3485 0399 3395 1954', 3500))
    wallet.append(CreditCard('Joe Doe', 'California Finance',
                             '5391 0375 9387 5309', 5000))
    pCC = PredatoryCreditCard('Joe Creditdoe', 'California Pred Finance',
                              '5391 0375 9387 5309', 5000, 0.15)
    wallet.append(pCC)

    for val in range(1, 64):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

    pCC.charge(3000)
    for x in range(12):
        pCC.process_month()
        print(f'Balance {x} {pCC.get_balance()}')


# Implement the sub method for the Vector class of Section 2.3.3, so
# that the expression u−v returns a new vector instance representing the
# difference between two vectors.

#    Implement the neg method for the Vector class of Section 2.3.3, so
# that the expression −v returns a new vector instance whose coordinates
# are all the negated values of the respective coordinates of v.

v1 = Vector(3)
v1[0] = 1
v1[1] = 3
v1[2] = 4
u = v1  # Calls v.__neg__() implicitly
print(u)  # Output: <-1, 2, -3>


# R-2.11 In Section 2.3.3, we note that our Vector class supports a syntax such as
# v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns
# a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal.
# Explain how the Vector class definition can be revised so that this syntax
# generates a new vector.


print(u+[12, 22, 32])
print([12, 22, 32] + u)
print(u*v1)


# Implement the mul method for the Vector class of Section 2.3.3, so
# that the expression u v returns a scalar that represents the dot product of
# the vectors, that is, ∑d
# i=1 ui · vi.


# The Vector class of Section 2.3.3 provides a constructor that takes an integer d, and produces a d-dimensional vector with all coordinates equal to
# 0. Another convenient form for creating a new vector would be to send the
# constructor a parameter that is some iterable type representing a sequence
# of numbers, and to create a vector with dimension equal to the length of
# that sequence and coordinates equal to the sequence values. For example,
# Vector([4, 7, 5]) would produce a three-dimensional vector with coordinates <4, 7, 5>. Modify the constructor so that either of these forms is
# acceptable; that is, if a single integer is sent, it produces a vector of that
# dimension with all zeros, but if a sequence of numbers is provided, it produces a vector with coordinates based on that sequence.


# R-2.16 Our Range class, from Section 2.3.5, relies on the formula
# max(0, (stop − start + step − 1) // step)

# R-2.18 Give a short fragment of Python code that uses the progression classes
# from Section 2.4.2 to find the 8th value of a Fibonacci progression that
# starts with 2 and 2 as its first two values.

class Progression:
    """Iterator producing a generic progression.

    Default iterator produces the whole numbers 0, 1, 2, ...
    """

    def __init__(self, start=0):
        """Initialize current to the first value of the progression."""
        self.current = start

    def advance(self):
        """Update self.current to a new value.

        This should be overridden by a subclass to customize progression.

        By convention, if current is set to None, this designates the
        end of a finite progression.
        """
        self.current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self.current is None:  # our convention to end a progression
            raise StopIteration()
        else:
            answer = self.current  # record current value to return
            self.advance()         # advance to prepare for next time
            return answer          # return the answer

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self

    def print_progression(self, n):
        """Print next n values of the progression."""
        print(' '.join(str(next(self)) for j in range(n)))


class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression."""

    def __init__(self, first=0, second=1):
        """Create a new fibonacci progression.

        first  the first term of the progression (default 0)
        second the second term of the progression (default 1)
        """
        super().__init__(first)  # start progression at first
        self.prev = second - first  # fictitious value preceding the first

    def advance(self):
        """Update current value by taking sum of previous two."""
        self.prev, self.current = self.current, self.prev + self.current


mafibo = FibonacciProgression(2, 2)
mafibo.print_progression(8)


# P-2.34 Write a Python program that inputs a document and then outputs a barchart
# plot of the frequencies of each alphabet character that appears in
# that document.

def calc_symbols(content):
    dict_of_symbols = {}
    for item in content:
        item = (item).lower()
        if item in dict_of_symbols.keys():
            dict_of_symbols[item] = dict_of_symbols[item] + 1
        else:
            dict_of_symbols[item] = 1
    return dict_of_symbols


try:
    with open('sample.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

letters_numbers = calc_symbols(content)

max_width = 40  # Max bar width

max_count = max(letters_numbers.values())
for key, value in sorted(letters_numbers.items()):
    bar = '*' * int((value / max_count) * max_width)
    # print(f"{key} | {bar} ({value})")


def parse_polynomial_to_list(polynomial):
    polynomial = polynomial.replace(" ", "")
    symbol_set = []
    members = []
    print(f'we get the string like {polynomial}')
    for ind in range(len(polynomial)):
        if ind == 0 or (polynomial[ind] not in ('+', '-')):
            if ind == 0 and polynomial[ind] not in ('+', '-'):
                symbol_set.append('+')
            symbol_set.append(polynomial[ind])
        elif ind > 0 and polynomial[ind] in ('+', '-'):
            members.append(''.join(symbol_set))
            symbol_set = []
            symbol_set.append(polynomial[ind])
        if ind+1 == len(polynomial):
            members.append(''.join(symbol_set))
    print(members)
    return members


def get_polynomial_apart(list_of_members):
    list_of_dicts = []
    for data in list_of_members:
        dict_member = {}
        dict_member['x'] = 'x'
        exponent_index = (data.find('^'))
        x_index = (data.find('x'))
        # we have the x and some number before the x - let's take it
        numberval = data[0:x_index]
        exponent_value = data[exponent_index+1:]
        dict_member['exponent'] = float(exponent_value)
        try:
            dict_member['number_val'] = float(numberval)
        except ValueError:
            dict_member['number_val'] = 1 if numberval == '+' else -1
        list_of_dicts.append(dict_member)
    return list_of_dicts


def get_derivative(list_of_dicts):
    new_str = ''
    for item in list_of_dicts:
        mult = item['number_val'] * item['exponent']
        new_exp = item['exponent'] - 1
        new_str = new_str + str(mult) + item['x'] + '^' + str(new_exp)
    return new_str

# Write a Python program that inputs a polynomial in standard algebraic
# notation and outputs the first derivative of that polynomial.


inputs = '4x^5 - 3x^2 + 2x^1 + 6x^0'
list_str = parse_polynomial_to_list(inputs)
list_dicts = get_polynomial_apart(list_str)
print(get_derivative(list_dicts))


# Write a set of Python classes that can simulate an Internet application in
# which one party, Alice, is periodically creating a set of packets that she
# wants to send to Bob. An Internet process is continually checking if Alice
# has any packets to send, and if so, it delivers them to Bob’s computer, and
# Bob is periodically checking if his computer has a packet from Alice, and,
# if so, he reads and deletes it.

def generate_random_name(length=6):
    # Define the possible characters: lowercase, uppercase, digits
    characters = string.ascii_letters + string.digits
    # Generate a random sequence of the specified length
    random_name = ''.join(random.choice(characters) for _ in range(length))
    return random_name


# Generate an 6-symbol random name
random_name = generate_random_name()


class package_dealer():
    def __init__(self, name):
        self.observers = []
        self.observer_names = []
        self.owned_packages = []

    def register_observer(self, observer):
        self.observers.append(observer)
        self.observer_names.append(observer.name)

    def deliver(self):
        for owned_package in self.owned_packages:
            for observer in self.observers:
                if owned_package.to_add == observer.name:
                    observer.recieve_package(owned_package)
                    self.owned_packages.remove(owned_package)

    def check_and_queue(self):
        for observer in self.observers:
            if len(observer.outgoing_packages) > 0:
                for delivery in observer.outgoing_packages:
                    if delivery.to_add in self.observer_names:
                        self.owned_packages.append(delivery)
                        observer.outgoing_packages.remove(delivery)
        if len(self.owned_packages) > 0:
            self.deliver()


class package():
    def __init__(self, from_add, to_add):
        self.status = 'new'
        self.from_add = from_add
        self.to_add = to_add
        self.hash = generate_random_name()

    def invalidate(self, invalidator):
        # if the operation is done by recepient
        if invalidator.name == self.to_add:
            self.status = 'archived'
        else:
            self.status = 'error'


class participant():

    def __init__(self, name):
        self.name = name
        self.archived_packages = []
        self.incoming_packages = []
        self.outgoing_packages = []

    def prep_package(self, to_addr):
        new_package = package(self.name, to_addr)
        self.outgoing_packages.append(new_package)

    def recieve_package(self, package):
        if package.status == 'new' and package.to_add == self.name:
            self.incoming_packages.append(package)
            self.read_package()

    def read_package(self):
        for x in self.incoming_packages:
            x.invalidate(self)
            self.archived_packages.append(x)


Internet = package_dealer('Internet')
Bob = participant('Bob')
Alice = participant('Alice')
Internet.register_observer(Bob)
Internet.register_observer(Alice)

Bob.prep_package('Alice')
Bob.prep_package('Alice')
Internet.check_and_queue()
print(Alice.archived_packages)
