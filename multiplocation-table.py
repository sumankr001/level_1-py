'''Multiplication Table:
Create a program that prints the multiplication table for a given number. For example, if the user inputs 5, the program should print the multiplication table for 5 (i.e., 5 x 1, 5 x 2, ..., 5 x 10).'''

number = int(input("Enter the number: "))

if number <=0 :
    print("please enter a positive integr")

else:
    print("please enter a number you wish to know the table")

for i in range(1, 11):
    result= i*number
    print("your table is: ", end='')
    print(f" {number}*{i} = {result}")




# for i in range (1,11):
#     if 

