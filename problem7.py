'''Base Conversion
Write a program that converts a number from one base to another. For instance, convert a decimal number into binary.

Example:
Input: 10 (decimal)
Output: 1010 (binary)
'''

decial_num = input("give any number:  ")
decial_num = int(decial_num)

binary_num = bin(decial_num)

print(binary_num)