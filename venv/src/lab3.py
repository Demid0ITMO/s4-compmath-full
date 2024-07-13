#!/bin/python3

import math
import os
import random
import re
import sys


def first_function(args: []) -> float:
    return 0.0


def second_function(args: []) -> float:
    return 0.0


def third_function(args: []) -> float:
    return pow(args[0], 2) * pow(args[1], 2) - 3 * pow(args[0], 3) - 6 * pow(args[1], 3) + 8


def fourth_function(args: []) -> float:
    return (pow(args[0], 4) + 2) / 9


def fifth_function(args: []) -> float:
    return args[0] + pow(args[0], 2) - 2 * args[1] * args[2] - 0.1


def six_function(args: []) -> float:
    return args[1] + pow(args[1], 2) + 3 * args[0] * args[2] + 0.2


def seven_function(args: []) -> float:
    return args[2] + pow(args[2], 2) + 2 * args[0] * args[1] - 0.3


def default_function(args: []) -> float:
    return 0.0


# How to use this function:
# funcs = Result.get_functions(4)
# funcs[0](0.01)
def get_functions(n: int):
    if n == 1:
        return [first_function, second_function]
    elif n == 2:
        return [third_function, fourth_function]
    elif n == 3:
        return [fifth_function, six_function, seven_function]
    else:
        return [default_function]


#
# Complete the 'solve_by_fixed_point_iterations' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts following parameters:
#  1. INTEGER system_id
#  2. INTEGER number_of_unknowns
#  3. DOUBLE_ARRAY initial_approximations
#

def solve_by_fixed_point_iterations(system_id, number_of_unknowns, initial_approximations):
    functions = get_functions(system_id)

    def iteration(x):
        delta = multiply_matrix_and_vector(
            inverse_matrix(get_jacobian(x)),
            [fun(x) for fun in functions]
        )
        return [x[i] - delta[i] for i in range(number_of_unknowns)]

    def get_jacobian(x):
        h = 1e-5
        jacobian = []
        for i in range(number_of_unknowns):
            row = []
            for j in range(number_of_unknowns):
                row.append((functions[i]([x[k] + (h if k == j else 0) for k in range(number_of_unknowns)]) - functions[
                    i](x)) / h)
            jacobian.append(row)
        return jacobian

    current_x = initial_approximations
    iterations = 1000
    epsilon = 1e-5
    while iterations > 0:
        new_x = iteration(current_x)
        sum_of_squares = sum((new_x[i] - current_x[i]) ** 2 for i in range(number_of_unknowns))
        if math.sqrt(sum_of_squares) < epsilon:
            return new_x
        current_x = new_x
        iterations -= 1
    raise IOError("Method is not applicable")


def multiply_matrix_and_vector(matrix, vector):
    return [sum(matrix[i][j] * vector[j] for j in range(number_of_unknowns)) for i in range(number_of_unknowns)]


def inverse_matrix(matrix):
    n = len(matrix)
    identity_matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    for i in range(n):
        if matrix[i][i] == 0:
            continue

        coefficient = matrix[i][i]
        for j in range(i, n):
            matrix[i][j] /= coefficient
        for j in range(n):
            identity_matrix[i][j] /= coefficient

        for k in range(i + 1, n):
            coefficient = matrix[k][i]
            for j in range(i, n):
                matrix[k][j] -= coefficient * matrix[i][j]
            for j in range(n):
                identity_matrix[k][j] -= coefficient * identity_matrix[i][j]

    for i in range(n - 1, 0, -1):
        for k in range(i - 1, -1, -1):
            coefficient = matrix[k][i]
            for j in range(n):
                identity_matrix[k][j] -= coefficient * identity_matrix[i][j]

    return identity_matrix


if __name__ == '__main__':
    system_id = int(input().strip())

    number_of_unknowns = int(input().strip())

    initial_approximations = []

    for _ in range(number_of_unknowns):
        initial_approximations_item = float(input().strip())
        initial_approximations.append(initial_approximations_item)

    result = solve_by_fixed_point_iterations(system_id, number_of_unknowns, initial_approximations)

    print('\n'.join(map(str, result)))
