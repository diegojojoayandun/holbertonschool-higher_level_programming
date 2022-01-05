#!/usr/bin/python3
def square_matrix_simple(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
          new_matrix = []
          [[j ** 2 for j in i] for i in matrix]
    return new_matrix
