# Write a Python Program to Check if given number is prime or not. 
# Also find factorial of the given no using user defined function.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(num):
    result = 1
    for i in range(1, num+1):
        result = result * i
    print(result)