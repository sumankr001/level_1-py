'''Sum of Numbers:
Write a program that calculates and prints the sum of all numbers from 1 to 100.'''


'''1. this is a very lenghty approach'''


# my_array=  list(range(1,101))
# sum = my_array[0]+ my_array[1]+ my_array[2] + and so on
# 
# print(sum)

# for in my_array[]>= 1 and my_array<= 101


my_array =  list(range(1, 101))

total_sum = 0

for elements in my_array:
    total_sum += elements

print("sum is :", total_sum)
