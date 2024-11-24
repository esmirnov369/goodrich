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
   