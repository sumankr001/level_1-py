''' Fibonacci Series
Write a program to print the first n terms of the Fibonacci series, where n is provided by the user.

Example:
Input: 6
Output: 0, 1, 1, 2, 3, 5'''

lst = []

def fabinacci(n):
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:

        return fabinacci(n-1) + fabinacci(n-2)
     

x = int(input("please enter the value of n: "))
print(fabinacci(x))

    



