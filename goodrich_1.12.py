import random

# Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise


def is_multiple(n: int, m: int):
    if n != 0:
        return (m/n).is_integer()
    else:
        return False

# Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.


def is_even(k: int):
    binary_str = str(format(k, 'b'))
    return (binary_str[-1] == '0')

# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution


def minmax(data):
    min = max = data[0]
    for x in data:
        if x > max:
            max = x
        if x < min:
            min = x
    return min, max

# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n


def sum_squares(n: int):
    sum = 0
    for x in range(1, n):

        sum = sum + (x*x)
    return sum

# R-1.5 Give a single command that computes the sum from Exercise R-1.4,
# relying on Python’s comprehension syntax and the built-in sum function.


def sum_squares_sugar(n: int):
    return sum([x*x for x in range(1, n)])

# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.


def odd_squares(n: int):
    sum = 0
    for x in range(1, n):
        if x % 2 != 0:
            sum = sum + (x*x)
    return sum

# Give a single command that computes the sum from Exercise R-1.6,
# relying on Python’s comprehension syntax and the built-in sum function.


def sum_odd_squares_sugar(n: int):
    return sum([x*x for x in range(1, n) if x % 2 != 0])

# Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0,
# what is the equivalent index j ≥ 0 such that s[j] references
# the same element?

# string s = 'ponytail' has len 8
# s[k] where -8<= k < 0 - e.g. -5
# n = (len('ponytail'))
# k = -5
# j = n + k
# print('ponytail'[k] == 'ponytail'[j])
# equivalent is j = n + k


# What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?
# print([x for x in range(50, 80+1, 10)])

# What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

# print([x for x in range(8, -8-1, -2)])

# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256]

# print([2*x for x in range(1, 10)])


# Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function.

a_list = ['a', 'b', 'c', 'd']
ranindex = random.randrange(0, len(a_list))


# Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.

def custom_rev(a_list: list):
    new_list = [None] * len(a_list)
    for x in range(0, len(a_list)):
        new_index = x
        rev_index = (x*-1)-1
        print(a_list[rev_index])
        new_list[new_index] = a_list[rev_index]
    return new_list


def custom_rev_comprehension(a_list: list):
    newlist = []
    newlist = [x for x in a_list[::-1]]
    return newlist


# print(custom_rev(["apple", "banana", "cherry", "delta", "epsilon"]))
# print(custom_rev_comprehension(
#    ["apple", "banana", "cherry", "delta", "epsilon"]))


# Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.

def pair_that_produces_odd(a_list: list):
    for i, vala in enumerate(a_list):
        for j, valb in enumerate(a_list):
            if i != j:
                if (vala * valb) % 2 != 0:
                    valuepair = vala, valb
                    return valuepair


# print(pair_that_produces_odd([1, 4]))

# Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct)


def are_all_items_unique(a_list: list):
    return (len(set(a_list)) == len(a_list))


a_list = ['a', 'ab', 'c', 'd']
# print(are_all_items_unique(a_list))

# In our implementation of the scale function (page 25), the body of the loop
# executes the command data[j] = factor. We have discussed that numeric
# types are immutable, and that use of the = operator in this context causes
# the creation of a new instance (not the mutation of an existing instance).
# How is it still possible, then, that our implementation of scale changes the
# actual parameter sent by the caller?


def scale(data, factor):
    for j in range(len(data)):
        data[j] = factor


a_list = [1, 2, 3, 4, 5]
scale(a_list, 5)
# print(a_list)

# it changes because we're modifying the list, not the numbers
# (but a function with no return statement is weird af for me anyways)


# C-1.17 Had we implemented the scale function (page 25) as follows, does it work
# properly?

def scale2(data, factor):
    for val in data:
        val = factor


a_list = [1, 2, 3, 4, 5]
scale2(a_list, 5)
# print(a_list)

# no, b/c numeric values are immutable

# C-1.18 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
x = [i * (i + 1) for i in range(10)]
# print(x)

# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally.


abc_list = [chr(x) for x in range(97, 97+26)]
# print(abc_list)

# Python’s random module includes a function shuffle(data) that accepts a
# list of elements and randomly reorders the elements so that each possible order occurs with equal probability. The random module includes a
# more basic function randint(a, b) that returns a uniformly random integer
# from a to b (including both endpoints). Using only the randint function,
# implement your own version of the shuffle function.


def custom_shuffle(my_list: list):
    newlist = []
    for x in range(len(my_list)):
        randindex = random.randint(0, len(my_list)-1)
        newlist.append(my_list.pop(randindex))
    return newlist


ma_list = ["apple", "banana", "cherry", "delta", "epsilon"]
# print(custom_shuffle(ma_list))

# Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D).

# for line in sys.stdin:
#  print(line[::-1])

# Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b. That is, it returns
# an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n−1


def get_dot_product(a_list: list, b_list: list):
    dot_list = [None] * len(a_list)
    for x in range(len(a_list)):
        dot_list[x] = a_list[x] * b_list[x]
    # realdotproudct = sum(dot_list)
    return dot_list


x = [1, 2, 3, 4]
y = [3, 4, 5, 6]
# print(get_dot_product(x, y))


# Give an example of a Python code fragment that attempts to write an element to a list based on an index that may be out of bounds. If that index
# is out of bounds, the program should catch the exception that results, and
# print the following error message:
# “Don’t try buffer overflow attacks in Python!”

err_list = [1, 2, 3]
try:
    err_list[3] = 4
except IndexError:
    print("Don’t try buffer overflow attacks in Python!")


# Write a short Python function that counts the number of vowels in a given
# character string.

def vowel_counter(string: str):
    count = 0
    vowels = 'aeiouAEIOU'
    a_list = list(string)
    for i in range(len(a_list)):
        if a_list[i] in vowels:
            count = count + 1
    return count


# print(vowel_counter("terrapin tester eats"))
