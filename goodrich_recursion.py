def draw_line(tick_length, tick_label=''):
    """Draw one line with given tick length (followed by optional label)."""
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    """Draw tick interval based upon a central tick length."""
    if center_length > 0:  # stop when length drops to 0
        draw_interval(center_length - 1)  # recursively draw top ticks
        draw_line(center_length)  # draw center tick
        draw_interval(center_length - 1)  # recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches, major tick length."""
    draw_line(major_length, '0')  # draw inch 0 line
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)  # draw interior ticks for inch
        draw_line(major_length, str(j))  # draw inch j line and label


#draw_ruler(5,3)




def calc_factorial(number):
    if number == 1:
        return number
    else:
        return number*calc_factorial(number-1)
    


# function that finds the minimum and maximum
#values in a sequence without using any loops.
def recursive_find_minmax(sequence,tempmax = None,tempmin=None):
    if tempmax is None or sequence[0] > tempmax:
        tempmax = sequence[0]
    if tempmin is None or sequence[0] < tempmin:
        tempmin = sequence[0]
    if len(sequence[1:])==0:
        return tempmax,tempmin
    else:
        rest_of_sequence = sequence[1:]        
        return recursive_find_minmax(rest_of_sequence,tempmax,tempmin)        

#print(recursive_find_minmax([1,66,-1]))         

#Describe a recursive algorithm to compute the integer part of the base-two
#logarithm of n using only addition and integer division.

def recursive_calcm(input_number,depth = 0):
    if input_number < 1:
        return depth
    else:
        return recursive_calcm(input_number//2,depth+1)    
    
result = recursive_calcm(10)
#print(result)    

#Describe an efficient recursive function for solving the element uniqueness
#problem, which runs in time that is at most O(n2) in the worst case
#without using sorting.

def el_unique(sequence):
    if  len(sequence) == 1:
        return True
    if sequence[0] in sequence[1:]:
        return False
    else:
        return el_unique(sequence[1:])
    
#print(el_unique([2,'y','7','y',0]))


#C-4.12 Give a recursive algorithm to compute the product of two positive integers,
#m and n, using only addition and subtraction.    

def recursive_product(m,n,product = 0):
    if n == 1:
        return product + m
    else:
        return recursive_product(m,n-1,product+m)

#print(recursive_product(33,3))        


#C-4.15 Write a recursive function that will output all the subsets of a set of n
#elements (without repeating any subsets).

def output_subsets(params_data):
    curr_subset = set()
    for item in params_data:
        curr_subset.add(item)
    print(curr_subset)

output_subsets({1,2,3,4})        