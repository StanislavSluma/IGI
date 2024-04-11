import matplotlib.pyplot as plt
import matplotlib.patches as ptch
from Checkinput import *
from Task_4.Trapezoid import Trapezoid


def complete_task4():
    trapezoid = Trapezoid()
    while True:
        print("0 >> exit")
        print("1 >> Enter params for trapezoid")
        print("2 >> Enter name")
        print("3 >> Enter color")
        print("4 >> Information")
        print("5 >> Plot")
        choose = input()
        if choose == "0":
            break
        elif choose == "1":
            print("Enter base a: ", end="")
            a = float_input(0, 0, False)
            if a <= 0:
                print("The value can not be a negative!")
                continue
            print("Enter base b: ", end="")
            b = float_input(0, 0, False)
            if b <= 0:
                print("The value can not be a negative!")
                continue
            print("Enter height h: ", end="")
            h = float_input(0, 0, False)
            if h <= 0:
                print("The value can not be a negative!")
                continue
            trapezoid.set_params(a, b, h)
        elif choose == "2":
            name = input("Enter name: ")
            trapezoid.set_name(name)
        elif choose == "3":
            color = input("Enter color: ")
            trapezoid.set_color(color)
        elif choose == "4":
            print(trapezoid)
            print(f"Area: {trapezoid.area()}")
        elif choose == "5":
            plt.xlim(0, max(trapezoid.get_params()))
            plt.ylim(0, max(trapezoid.get_params()))
            axes = plt.gca()
            axes.set_aspect("equal")
            #print(trapezoid.get_points())
            polygon = ptch.Polygon(trapezoid.get_points(), color=trapezoid.get_color())
            axes.add_patch(polygon)
            plt.xlabel(f"{trapezoid.get_name()}")
            plt.savefig('Task_4/figure_with_legend.png')
            plt.show()
        else:
            print("Enter only 0, 1, 2, 3, 4!")
            input("Enter to continue...")
