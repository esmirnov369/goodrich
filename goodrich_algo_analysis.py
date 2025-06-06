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


x = prefix_average1(sample_data)
end = time.perf_counter()
print(f"Elapsed time: {end - start:.6f} seconds")

start = time.perf_counter()
z = prefix_average2(sample_data)
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
plt.plot(n, y0, label='8 n', color='blue')
plt.plot(n, y1, label='2 n squared', color='red')
plt.plot(n, y2, label=' 4 n log n', color='green')
plt.plot(n, y3, label=' n to the 3rd', color='yellow')
# plt.plot(n, y4, label=' 2 to the n2th', color='grey')

plt.title('Plot all kins of n')
plt.xlabel('n')
plt.ylabel('progress')
plt.grid(True)
plt.legend()
plt.show()
