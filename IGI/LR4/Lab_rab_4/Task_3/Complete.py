from Checkinput import *
from Task_3.ExtraOptions import *
import math
import matplotlib.pyplot as plt
import numpy as np


def complete_task3():
    while True:
        print("0 >> exit")
        print("1 >> Enter collection")
        print("2 >> Plot function")
        choose = input()
        if choose == "0":
            break
        elif choose == "1":
            print("Size of array: ", end="")
            size = int_input(1, 16)
            coll = list()
            for i in range(0, size):
                coll.append(float_input(0.0, 0.0, False))
            print(f"Average value: {ExtraOptions.average(coll)}")
            print(f"Median value: {ExtraOptions.median(coll)}")
            print("Moda value: ")
            moda = ExtraOptions.moda(coll)
            if len(moda) == 0:
                print("All values are unique")
            else:
                for el in moda:
                    print(el, end=" ")
                print()
            print(f"Dispersion value: {ExtraOptions.dispersion(coll)}")
            print(f"Standard deviation value: {ExtraOptions.standard_deviation(coll)}")
        elif choose == "2":
            print("MathFunc: ln(1 + x), |x| < 1")
            print("Enter amount of points: ", end="")
            point_amount = int_input(3, 1000)
            print("Enter eps: ", end="")
            eps = float_input(0.0001, 1, True)
            h = 0.99 / point_amount
            x = np.arange(0, 1, h)
            tailor_res = list()
            try:
                for xi in x:
                    tailor_res.append((tailor_func(xi, eps))[0])
            except ValueError:
                print("Warning!!! Exception: ValueError")
                input("Enter to continue...")
                break
            y = np.log(1 + x)
            plt.plot(x, tailor_res, label=r'Taylor')
            plt.plot(x, y, label=r'$log(1+x)$')
            plt.xlabel(r'$x$')
            plt.ylabel(r'$f(x)$')
            plt.legend(loc='best', fontsize=8)
            plt.savefig('Task_3/figure_with_legend.png')
            plt.show()
        else:
            print("Enter only 0, 1, 2, 3, 4!")
            input("Enter to continue...")


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
        an = (-1) ** ((n - 1) % 2) * (x ** n) / n
        res += an
        if abs(an) < eps:
            return res, n
        n += 1
    return res, n
