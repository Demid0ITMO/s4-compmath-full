#!/bin/python3


def interpolate_by_newton(x_axis, y_axis, x):
    try:
        n = len(x_axis)
        matrix = [[0.0] * n for i in range(n)]
        for i in range(n):
            matrix[i][0] = y_axis[i]
        for j in range(1, n):
            for i in range(n-j):
                matrix[i][j] = (matrix[i+1][j-1] - matrix[i][j-1]) / (x_axis[i+j] - x_axis[i])
        n = n - 1
        polynom = matrix[0][n]
        for i in range(1, n + 1):
            polynom = matrix[0][n - i] + (x - x_axis[n - i]) * polynom
        return polynom
    except:
        return None


if __name__ == '__main__':
    axis_count = int(input().strip())

    x_axis = list(map(float, input().rstrip().split()))

    y_axis = list(map(float, input().rstrip().split()))

    x = float(input().strip())

    result = interpolate_by_newton(x_axis, y_axis, x)

    print(str(result) + '\n')
