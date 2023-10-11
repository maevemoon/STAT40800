import numpy as np

# exercise 4
def factorial(x):
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

x = 5
print(factorial(x))

# exercise 5
def multiples_three(n):
    array = np.arange(1, n+1) * 3
    return array

n = 5
print(multiples_three(n))

# exercise 6
def matrix_index(x,n,m):
    return x[n,m]

x = np.array([7,3,1,9]).reshape(2,2)
n = 0
m = 1
print(matrix_index(x,n,m))

# converting decimal to binary using bitwise operators
def binary_conversion(x):
    list = []
    while x:
        list.append(x&1)
        x = x >> 1
    
    list = list[::-1]
    return list

# converting decimal to binary without using bitwise operators
def binary_conversion(x):
    list = []
    while x > 0:
        remainder = x % 2
        # insert before certain index; aka inserting backwards
        # can append() and then [::-1] though
        list.insert(0,remainder)
        x //= 2
    
    return list