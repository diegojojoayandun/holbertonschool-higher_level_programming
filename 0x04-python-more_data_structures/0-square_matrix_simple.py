#!/usr/bin/python3
def square_matrix_simple(matrix=[[]]):

    new_matrix = [[j ** 2 for j in i] for i in matrix]
    return new_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)