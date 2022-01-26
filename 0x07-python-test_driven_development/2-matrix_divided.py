#!/usr/bin/python3
"""Module matrix_divided
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix
    """
    new_matrix = []
    raise_err = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(raise_err)

    for i in range(len(matrix)):
        if check_lenght_rows(matrix) is False:
            raise TypeError("Each row of the matrix must have the same size")
        tmp_list = []
        for j in range(len(matrix[i])):
            if isinstance(matrix[i][j], (float, int)) is not True:
                raise TypeError(raise_err)
            if check_div_non_int_float(div) is False:
                raise TypeError("div must be a number")
            if check_div_non_zero is False:
                raise ZeroDivisionError("division by zero")

            tmp_list.append(round((matrix[i][j]) / div, 2))
        new_matrix.append(tmp_list)
    return new_matrix


def check_lenght_rows(matrix):
    """checks if rows have same lenght"""
    for sub_list in matrix:
        if len(matrix[0]) != len(sub_list):
            return False


def check_div_non_int_float(div):
    """checks if div is not zero
    and if it's a integer
    """
    if isinstance(div, (int, float)) is not True:
        return False


def check_div_non_zero(div):
    """checks if div is not zero
    and if it's a integer
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
