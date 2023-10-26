'''Fibonacci Sequence:
Generate and print the first 10 numbers in the Fibonacci sequence. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding numbers.'''


from math import *
from collections import *
from sys import *
from os import *

n=int(input())

a,b = 1,1

if n == 1 and n== 2:

    print(1)

else:

    for _ in range(1,n):

        c= a+b

        a=b

        b=c

print(a)