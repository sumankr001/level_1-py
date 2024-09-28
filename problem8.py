'''Factorial Calculation
Write a program to compute the factorial of a number using recursion.

Example:
Input: 5
Output: 5! = 120
'''


def factorial_num(n):
    if n == 0:
        return 1
    
    else:
        return n * factorial_num(n-1)
    

print(factorial_num(3))