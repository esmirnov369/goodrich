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

