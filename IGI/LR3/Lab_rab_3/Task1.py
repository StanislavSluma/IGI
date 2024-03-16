
#Составить программу для вычисления значения функции c помощью разложения функции в степенной ряд.
#Задать точность вычислений eps.


def func_decorator(input_func):
    def output_func(*args):
        print("Counting...")
        res, n = input_func(*args)
        if n == 501:
            print("Number of iterations exceeded")
        else:
            print("Success")
        return res, n
    return output_func


@func_decorator
def tailor_func(x: float, eps: float):  # ln(1 + x)
    """
    :param x: function variable
    :param eps: accuracy of calculation
    :return:
    res - result of calculation with established accuracy
    if iterations amount exceeded return result of 500 iterations;
    n - number of iterations;
    """
    res = 0.0
    n = 1
    while n <= 500:
        an = (-1)**((n-1) % 2) * (x**n) / n
        res += an
        if abs(an) < eps:
            return res, n
        n += 1
    return res, n
