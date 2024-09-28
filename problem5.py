'''Prime Factors
Write a program to find the prime factors of a given number.

Example:
Input: 28
Output: [2, 2, 7]
'''

num = input("enter the number: ")

def prime_factor(num, x):
    while num % x == 0:
        for i in range(2,x):
            if x%i == 0:
                return False
                break
            else:
                return False           
        return x
        

