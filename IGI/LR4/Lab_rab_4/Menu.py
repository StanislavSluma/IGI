from Task_1.Complete import complete_task1
from Task_2.Complete import complete_task2
from Task_3.Complete import complete_task3
from Task_4.Complete import complete_task4
from Task_5.Complete import complete_task5


def menu():
    print("LAB_RAB_4")
    print("Enter a number to continue\n")
    while True:
        print("0 >> exit")
        print("1 >> Task1 (Library)")
        print("2 >> Task2 (Text)")
        print("3 >> Task3 (Plot)")
        print("4 >> Task4 (Figures)")
        print("5 >> Task5 (NumPy)")
        choose = input()
        if choose == "0":
            break
        elif choose == "1":
            complete_task1()
        elif choose == "2":
            complete_task2()
        elif choose == "3":
            complete_task3()
        elif choose == "4":
            complete_task4()
        elif choose == "5":
            complete_task5()
        else:
            print("Enter only 0, 1, 2, 3, 4, 5!")

