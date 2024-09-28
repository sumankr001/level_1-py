"""rite a program to find the Least Common Multiple (LCM) and the Greatest Common Divisor (GCD) of two numbers.

Example:
Input: 12, 18
Output: LCM = 36, GCD = 6
"""

import math

number = input("enter two numbers:  ")

a,b = map(int, number.split())
lcm1 = math.lcm(a,b)
print(lcm1)


gcd1 = math.gcd(a,b)
print(gcd1)