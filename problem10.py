'''Sum of N Natural Numbers
Write a program to find the sum of the first n natural numbers using the formula n(n+1)/2.

Example:
Input: 5
Output: 15
(Explanation: 1 + 2 + 3 + 4 + 5 = 15)'''

def natural_num(n):
    if n == 1:
        return 1
    
    else:
        return n * (n+1) //2

n =int(input("enter the value of n: "))
print(natural_num(n))