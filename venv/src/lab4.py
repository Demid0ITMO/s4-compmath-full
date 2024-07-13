import math


class Result:
    error_message = "Integrated function has discontinuity or does not defined in current interval"
    has_discontinuity = False

    def first_function(x: float):
        return 1 / x

    def second_function(x: float):
        if x == 0:
            return (math.sin(Result.eps)/Result.eps + math.sin(-Result.eps)/-Result.eps)/2
        return math.sin(x)/x

    def third_function(x: float):
        return x*x+2

    def fourth_function(x: float):
        return 2*x+2

    def five_function(x: float):
        return math.log(x)

    def test(x: float):
        return math.sqrt(x**2 + 3)

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
        elif n == 5:
            return Result.five_function
        else:
            raise NotImplementedError(f"Function {n} not defined.")

    #
    # Complete the 'calculate_integral' function below.
    #
    # The function is expected to return a DOUBLE.
    # The function accepts following parameters:
    #  1. DOUBLE a
    #  2. DOUBLE b
    #  3. INTEGER f
    #  4. DOUBLE epsilon
    #

    def calculate_integral(a, b, f, epsilon):
        function = Result.get_function(f)
        sign = 1
        if a > b:
            sign = -1

        def calculate_simpson_formula_for_n(n, left, right):
            h = float((right - left) / n)
            f_values = [function(left + i * h) for i in range(0, n + 1)]
            return h / 3 * (f_values[0] +
                            f_values[n] +
                            sum(x for i, x in enumerate(f_values[1:n]) if i % 2 == 0) * 2 +
                            sum(x for i, x in enumerate(f_values[1:n]) if i % 2 == 1) * 4)

        try:
            splits_counter = 2
            answer = calculate_simpson_formula_for_n(splits_counter, min(a, b), max(a, b))
            while True:
                splits_counter *= 2
                new_answer = calculate_simpson_formula_for_n(splits_counter, min(a, b), max(a, b))
                if abs(new_answer - answer) <= epsilon:
                    return new_answer * sign
                answer = new_answer
        except:
            Result.has_discontinuity = True
            return 0


if __name__ == '__main__':

    a = float(input().strip())

    b = float(input().strip())

    f = int(input().strip())

    epsilon = float(input().strip())

    result = Result.calculate_integral(a, b, f, epsilon)
    if not Result.has_discontinuity:
        print(str(result) + '\n')
    else:
        print(Result.error_message + '\n')
