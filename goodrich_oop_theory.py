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

#Use the techniques of Section 1.7 to revise the charge and make payment
#methods of the CreditCard class to ensure that the caller sends a number
#as a parameter

#R-2.6 If the parameter to the make payment method of the CreditCard class
#were a negative number, that would have the effect of raising the balance
#on the account. Revise the implementation so that it raises a ValueError if
#a negative value is sent.

#R-2.7 The CreditCard class of Section 2.3 initializes the balance of a new account to zero. Modify that class so that a new account can be given a
#nonzero balance using an optional fifth parameter to the constructor. The
#four-parameter constructor syntax should continue to produce an account
#with zero balance.

#R-2.8 Modify the declaration of the first for loop in the CreditCard tests, from
#Code Fragment 2.3, so that it will eventually cause exactly one of the three
#credit cards to go over its credit limit. Which credit card is it?


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
        

class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self.coords = [0] * d

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
    
    def __radd__(self,other):
        """Return sum of two vectors."""
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    

    def __mul__(self,multiplier):
        if isinstance(multiplier,int):
            result = Vector(len(self))  # start with vector of zeros
            for j in range(len(self)):
                result[j] = self[j]* multiplier
            return result    
        elif isinstance(multiplier,Vector) & len(multiplier) == len(self) :
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

    for val in range(1, 64):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        #while wallet[c].get_balance() > 100:
           # wallet[c].make_payment(100)
            #print('New balance =', wallet[c].get_balance())
        #print()



#Implement the sub method for the Vector class of Section 2.3.3, so
#that the expression u−v returns a new vector instance representing the
#difference between two vectors.

#    Implement the neg method for the Vector class of Section 2.3.3, so
# that the expression −v returns a new vector instance whose coordinates
# are all the negated values of the respective coordinates of v.

v1 = Vector(3)
v1[0] = 1
v1[1] = 3
v1[2] = 4
u = v1  # Calls v.__neg__() implicitly
print(u)  # Output: <-1, 2, -3>


#R-2.11 In Section 2.3.3, we note that our Vector class supports a syntax such as
#v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns
#a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal.
#Explain how the Vector class definition can be revised so that this syntax
#generates a new vector.


print(u+[12,22,32])
print([12,22,32] + u)
print(u*v1)


#Implement the mul method for the Vector class of Section 2.3.3, so
#that the expression u v returns a scalar that represents the dot product of
#the vectors, that is, ∑d
#i=1 ui · vi.