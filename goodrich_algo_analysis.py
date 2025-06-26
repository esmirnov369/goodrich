import matplotlib.pyplot as plt
import numpy as np
import random
import time


# List of 1000 random integers between 1 and 100
sample_data = [random.randint(1, 100) for _ in range(10000)]


def prefix_average1(values_list):
    # Return list such that, for all j, A[j] equals average of S[0], ..., S[j].”””
    n = len(values_list)
    prefixed_list = [0] * n  # create new list of n zeros
    for j in range(n):
        total = 0  # begin computing S[0] + ... + S[j]
        for i in range(j + 1):
            total += values_list[i]
            prefixed_list[j] = total / (j+1)  # record the average
    return prefixed_list


def prefix_average2(values_list):
    prefixed_array = [0] * len(values_list)
    presum = 0
    for x in range(len(values_list)):
        presum = presum + values_list[x]
        prefixed_array[x] = presum / (x + 1)
    return prefixed_array


start = time.perf_counter()
#x = prefix_average1(sample_data)
end = time.perf_counter()
print(f"Elapsed time: {end - start:.6f} seconds")
start = time.perf_counter()
#z = prefix_average2(sample_data)
end = time.perf_counter()
print(f"Elapsed time: {end - start:.6f} seconds")


def unique1(S):
    """Return True if there are no duplicate elements in sequence S."""
    for j in range(len(S)):
        for k in range(j + 1, len(S)):
            if S[j] == S[k]:
                return False  # Found a duplicate pair
    return True  # No duplicates found


# Graph the functions 8n, 4nlogn, 2n2, n3, and 2n using a logarithmic scale
# for the x- and y-axes; that is, if the function value f(n) is y, plot this as a
# point with x-coordinate at logn and y-coordinate at logy.


# Generate values for n
n = np.linspace(1, 20, 400)  # from 1 to 50, with 400 points

# Compute log(n)
y0 = 8 * n
y1 = 2 * n**2
y2 = 4 * n * np.log(n)
y3 = n**3
y4 = 2**n

# Plot
if 1 > 2:
    plt.plot(n, y0, label='8 n', color='blue')
    plt.plot(n, y1, label='2 n squared', color='red')
    plt.plot(n, y2, label=' 4 n log n', color='green')
    plt.plot(n, y3, label=' n to the 3rd', color='yellow')
    plt.plot(n, y4, label=' 2 to the n2th', color='grey')

    plt.title('Plot all kins of n')
    plt.xlabel('n')
    plt.ylabel('progress')
    plt.grid(True)
    plt.legend()
    plt.show()


    x = np.linspace(1, 20, 400)  # from 1 to 50, with 400 points

    B =  2 * x**2
    A = 8 * x * np.log2(x)
    plt.plot(x, B, label='B', color='blue')
    plt.plot(x, A, label='A', color='red')
    plt.title('Plot the results')
    plt.xlabel('n')
    plt.ylabel('progress')
    plt.grid(True)
    plt.legend()
    plt.show()



#The number of operations executed by algorithms A and B is 40n2 and
#2n3, respectively. Determine n0 such that A is better than B for n ≥ n0.

# 40 * x**2 == 2*x**3
# 40x**2 - 2x**3 = 0
# 2x**2(n-20) = 0
# x = 0 or x = 20, probably 20 - checking 

x = np.linspace(1, 50, 400)  # from 1 to 50, with 400 points

A = 40 * x**2
B = 2*x**3


plt.plot(x, A, label='A', color='red')
plt.plot(x, B, label='B', color='blue')
plt.title('Plot the results')
plt.xlabel('n')
plt.ylabel('progress')
plt.grid(True)
plt.legend()
plt.show()


#R-3.4 Give an example of a function that is plotted the same on a log-log scale
#as it is on a standard scale.


#Give a big-Oh characterization, in terms of n, of the running time of the
#example1 function shown in Code Fragment 3.10.

def example1(S):
    """Return the sum of the elements in sequence S."""
    total = 0
    for num in S:  # Directly iterate over elements (more Pythonic)
        total += num
    return total

#translates to N

def example2(S):
    """Return the sum of the elements with even index in sequence S."""
    total = 0
    for j in range(0, len(S), 2):  # Step by 2 to get even indices
        total += S[j]
    return total

# translates to N/2 which is also N


def example3(S):
    """Return the sum of the prefix sums of sequence S."""
    total = 0
    for j in range(len(S)):
        for k in range(j + 1):
            total += S[k]
    return total

#translates to n**2


def example4(S):
    """Return the sum of the prefix sums of sequence S."""
    prefix = 0
    total = 0
    for num in S:  # More Pythonic than range(len(S))
        prefix += num
        total += prefix
    return total

# translates to N


def example5(A, B):
    """Return the number of elements in B equal to the sum of prefix sums in A."""
    n = len(A)
    count = 0
    for i in range(n):  # loop from 0 to n-1
        total = 0
        for j in range(n):  # loop from 0 to n-1
            for k in range(1 + j):  # loop from 0 to j
                total += A[k]
        if B[i] == total:
            count += 1
    return count

#translates to n**3


#Al and Bob are arguing about their algorithms. Al claims his O(nlogn)-
#time method is always faster than Bob’s O(n2)-time method. To settle the
#issue, they perform a set of experiments. To Al’s dismay, they find that if
#n < 100, the O(n2)-time algorithm runs faster, and only when n ≥ 100 is
#the O(nlogn)-time one better. Explain how this is possible.

#this is possible when there's a small data set 


#Assuming it is possible to sort n numbers in O(nlog n) time, show that it
#is possible to solve the three-way set disjointness problem in O(nlogn)
#time.


ideal_sorted_set1 = [1,2,3]
ideal_sorted_set2 = [3,2,5]
ideal_sorted_set3 = [1,1.5,2]

def binary_search(set,item):
    return True

def nlogn_3wayset(set1,set2,set3):
    for item in set1:
        if binary_search(set2,item):
            return binary_search(set3,item)
        
#translates to n log n 
# 
# 
# Describe an efficient algorithm for finding the ten largest elements in a
#sequence of size n. What is the running time of your algorithm?        

#the running time is roughly equal to any decent sorting algo (n log n)
#or can do heap

sequence = [1,2,3,4,5,3,3,12,3,4,5,6,7,8,98,5,4,3,35,6,7,8,9]
heap = []

def find_min_max(sequence):
    temp_min = temp_max = sequence[0]
    for number in range(0,len(sequence),2):
        a,b = sequence[number],sequence[number+1]
        b = sequence[number+1] if (number+1 < len(sequence)) else None  # Avoid IndexError
        if b is not None:  # Even-length pair
            if a > b:
                if a > temp_max:
                    temp_max = a
                if b < temp_min:
                    temp_min = b
            else:
                if b > temp_max:
                    temp_max = b
                if a < temp_min:
                    temp_min = a
        else:
            if a > temp_max: temp_max = a
            elif a < temp_min: temp_min = a             
    return temp_min, temp_max        




#A sequence S contains n−1 unique integers in the range [0,n−1], that
#is, there is one number from this range that is not in S. Design an O(n)-
#time algorithm for finding that number. You are only allowed to use O(1)
#additional space besides the sequence S itself.

n = 5
number_not_in_seq = 2
#init seq of len n-1 unique ints in range 0,n-1
seq_S = [0,1,3,4]

num_found = None

expected_sum = (n*(n-1))//2
actual_sum = 0
for number in seq_S:
    actual_sum = actual_sum + number

print(expected_sum - actual_sum)


def bad_fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n - 2) + bad_fibonacci(n - 1)
    
print(bad_fibonacci(6))
