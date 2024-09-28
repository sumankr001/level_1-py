"""Reverse a Number
Write a program to reverse a given integer without converting it into a string.

Example:
Input: 1234
Output: 4321"""


# soln:
'''sequence[start:stop:step]'''

"""[::-1] Specifically:
The absence of start and stop means the entire sequence is considered.
The step -1 means the sequence will be traversed from end to beginning, effectively reversing it."""


number = input("please enter the number:~ ")

print(number[::-1])