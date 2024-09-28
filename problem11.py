'''Quadratic Equation Solver
Write a program to solve a quadratic equation ax^2 + bx + c = 0 using the quadratic formula:
x = (-b ± sqrt(b^2 - 4ac)) / 2a.

Example:
Input: a = 1, b = -3, c = 2
Output: x = 2, x = 1'''

import math

def quadratic(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant< 0:
        return 'no real roots'
           
    elif a == 0 or b == 0:
        return c
    
    else:
        root1 = (-b + math.sqrt(b**2 - 4* a* c)) / 2* a
        root2 = (-b - math.sqrt(b**2 - 4* a* c)) / 2* a
        return root1, root2
    

print(quadratic(7, 6, 3))

