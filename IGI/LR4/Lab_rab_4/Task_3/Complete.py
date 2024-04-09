from Checkinput import *
from Task_3.ExtraOptions import *


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
            print("mama")
        else:
            print("Enter only 0, 1, 2, 3, 4!")
            input("Enter to continue...")
