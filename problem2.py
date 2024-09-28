'''Problem: Matrix Flattening with Conditional Filtering
You are given a 2D matrix (list of lists) of integers. Your task is to write a list comprehension that:

Flattens the 2D matrix into a 1D list.
Filters the numbers that are divisible by 3 or 5.
Squares the filtered numbers.

Example:
matrix = [
    [1, 5, 9],
    [2, 10, 15],
    [4, 12, 18]
]

Expected Output:
[25, 81, 100, 225, 144, 324]'''

"""task 1"""

matrix = [
    [1, 5, 9],
    [2, 10, 15],
    [4, 12, 18]
]


"""item = matrix[2][2]---used for accesing any element of a matrix"""

matrix1 = []

for row in matrix:
    for elements in row:
        matrix1.append(elements)

print(matrix1)

"""task 2: Filters the numbers that are divisible by 3 or 5."""

matrix2 = []

for n in matrix1:
    if n % 3 ==0 or n % 5 ==0:
        matrix2.append(n)

print(matrix2)


"""task3 : Squares the filtered numbers"""

# using list comprehension method
matrix3 = [num**2 for num in matrix2]
print(matrix3)

