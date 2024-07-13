import math


class Result:

    def first_function(x: float, y: float):
        return math.sin(x)


    def second_function(x: float, y: float):
        return (x * y)/2


    def third_function(x: float, y: float):
        return y - (2 * x)/y


    def fourth_function(x: float, y: float):
        return x + y


    def default_function(x:float, y: float):
        return 0.75 * pow(math.e, -2 * x) + 0.5 * pow(x, 2) - 0.5 * x + 0.25

    # How to use this function:
    # func = Result.get_function(4)
    # func(0.01)
    def get_function(n: int):
        if n == 1:
            return Result.first_function
        elif n == 2:
            return Result.second_function
        elif n == 3:
            return Result.third_function
        elif n == 4:
            return Result.fourth_function
        else:
            return Result.default_function

    #
    # Complete the 'solveByEulerImproved' function below.
    #
    # The function is expected to return a DOUBLE.
    # The function accepts following parameters:
    #  1. INTEGER f
    #  2. DOUBLE epsilon
    #  3. DOUBLE a
    #  4. DOUBLE y_a
    #  5. DOUBLE b
    #
    def solveByEulerImproved(f, epsilon, a, y_a, b):
        function = Result.get_function(f)
        h = 0.1
        x = a
        y = y_a

        while x < b:
            prev_y = y + h * function(x, y)
            corrected_y = y + h / 2 * (function(x, y) + function(x + h, prev_y))

            if abs(prev_y - corrected_y) < epsilon:
                y = corrected_y
                x += h

            h *= 0.9 * pow(epsilon / abs(prev_y - corrected_y), 0.2)

            if x + h > b:
                h = b - x

        return y


if __name__ == '__main__':
    f = int(input().strip())

    epsilon = float(input().strip())

    a = float(input().strip())

    y_a = float(input().strip())

    b = float(input().strip())

    result = Result.solveByEulerImproved(f, epsilon, a, y_a, b)

    print(str(result) + '\n')
