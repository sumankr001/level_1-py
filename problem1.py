"""1. Sum of Digits of a Number
Write a program to find the sum of the digits of a given positive integer.

Example:
Input: 234
Output: 2 + 3 + 4 = 9"""


num = input("please enter your desired whole number: ")

# see here i have converted the input into a list, although input is string
list_number = list(num)

# then we have to convert each iterated elements of list_number into integer 
int_sum = [int(n) for n in list_number]
total = sum(int_sum)
print(total)

# result = sum(list_number)

# print(result)
