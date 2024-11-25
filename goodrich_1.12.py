import random
#Write a short Python function, is multiple(n, m), that takes two integer
#values and returns True if n is a multiple of m, that is, n = mi for some
#integer i, and False otherwise

def is_multiple(n :int, m :int):
    if n != 0:
        return (m/n).is_integer()
    else:
        return False    

#Write a short Python function, is even(k), that takes an integer value and
#returns True if k is even, and False otherwise. However, your function
#cannot use the multiplication, modulo, or division operators.

def is_even(k :int):
    binary_str = str(format(k, 'b'))
    return (binary_str[-1] == '0')

#Write a short Python function, minmax(data), that takes a sequence of
#one or more numbers, and returns the smallest and largest numbers, in the
#form of a tuple of length two. Do not use the built-in functions min or
#max in implementing your solution

def minmax(data):
    min = max = data[0]
    for x in data:
     if x > max:
         max = x
     if x < min:
         min = x
    return min,max  

#Write a short Python function that takes a positive integer n and returns
#the sum of the squares of all the positive integers smaller than n  
def sum_squares(n :int):
    sum = 0
    for x in range(1,n):

        sum = sum + (x*x)
    return sum

#R-1.5 Give a single command that computes the sum from Exercise R-1.4, 
# relying on Python’s comprehension syntax and the built-in sum function.

def sum_squares_sugar(n :int):
    return sum([x*x for x in range(1,n)])

#Write a short Python function that takes a positive integer n and returns
#the sum of the squares of all the odd positive integers smaller than n.

def odd_squares(n: int):
    sum = 0
    for x in range(1,n):
        if x % 2 != 0:
            sum = sum + (x*x)
    return sum

#Give a single command that computes the sum from Exercise R-1.6, 
#relying on Python’s comprehension syntax and the built-in sum function.
def sum_odd_squares_sugar(n :int):
    return sum([x*x for x in range(1,n) if x % 2 != 0])

#Python allows negative integers to be used as indices into a sequence,
#such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0, 
#what is the equivalent index j ≥ 0 such that s[j] references
#the same element?

#string s = 'ponytail' has len 8 
#s[k] where -8<= k < 0 - e.g. -5
#n = (len('ponytail'))
#k = -5
#j = n + k
#print('ponytail'[k] == 'ponytail'[j])
#equivalent is j = n + k

#What parameters should be sent to the range constructor, to produce a
#range with values 50, 60, 70, 80?

#Demonstrate how to use Python’s list comprehension syntax to produce
#the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
print([2**x for x in range(1,8+1)])

#Python’s random module includes a function choice(data) that returns a
#random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to
#the built-in range function, that return a random choice from the given
#range. Using only the randrange function, implement your own version
#of the choice function.

a_list = ['a','b','c','d']
ranindex = random.randrange(0,len(a_list))


#Write a pseudo-code description of a function that reverses a list of n
#integers, so that the numbers are listed in the opposite order than they
#were before, and compare this method to an equivalent Python function
#for doing the same thing.

def custom_rev(a_list: list):
    new_list = [None] * len(a_list)
    for x in range(0,len(a_list)):
        new_index = x
        rev_index = (x*-1)-1    
        print(a_list[rev_index])
        new_list[new_index] = a_list[rev_index]
    return new_list    

print(custom_rev(["apple", "banana", "cherry", "delta", "epsilon"]))