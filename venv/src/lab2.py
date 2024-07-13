#!/bin/python3


class Result:
    isMethodApplicable = True
    errorMessage = "The system has no diagonal dominance for this method. Method of the Gauss-Seidel is not applicable."

    def solveByGaussSeidel(n, matrix, epsilon):
        try:
            if not Result.isDDM(n, matrix):
                Result.isMethodApplicable = False
                return []
            x_values = [0 for _ in range(n)]
            residuals = [0 for _ in range(n)]
            max_difference = epsilon + 1
            while max_difference > epsilon:
                max_difference = 0
                for i in range(n):
                    iteration_sum = 0
                    for j in range(n):
                        iteration_sum += matrix[i][j] * x_values[j]
                    residuals[i] = (iteration_sum - matrix[i][n]) / matrix[i][i]
                    x_values[i] -= residuals[i]
                    max_difference = max(max_difference, abs(residuals[i]))
            return x_values
        except:
            Result.isMethodApplicable = False
            return []

    def isDDM(n, matrix):
        for i in range(n):
            sum_of_abs_row_elements = 0
            for j in range(n):
                sum_of_abs_row_elements = sum_of_abs_row_elements + abs(matrix[i][j])
            if sum_of_abs_row_elements >= 2 * abs(matrix[i][i]):
                return False
        return True


if __name__ == '__main__':
    n = int(input().strip())

    matrix_rows = n
    matrix_columns = n+1

    matrix = []

    for _ in range(matrix_rows):
        matrix.append(list(map(float, input().rstrip().split())))

    epsilon = float(input().strip())

    result = Result.solveByGaussSeidel(n, matrix, epsilon)
    if Result.isMethodApplicable:
        print('\n'.join(map(str, result)))
    else:
        print(f"{Result.errorMessage}")
