import math
import random
from CheckInput import *
from Task1 import tailor_func
from Task2 import cycle
from Task3 import is_hex
from Task4 import text_analyze
from Task5 import list_analyze


def menu():
    while True:
        print("\n")
        print("Enter 0 >>> exit")
        print("Enter 1 >>> Task1 (Tailor_Func)")
        print("Enter 2 >>> Task2 (Sum cycle)")
        print("Enter 3 >>> Task3 (Is HEX)")
        print("Enter 4 >>> Task4 (Text analyze)")
        print("Enter 5 >>> Task5 (Float_list)")
        choose = input()
        if choose == "0":
            print("Goodbye!")
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


def complete_task1():
    print("*"*20)
    print("MathFunc: ln(1 + x), |x| < 1")
    print("Enter x: ", end="")
    x = float_input(-1, 1, True)
    print("Enter eps: ", end="")
    eps = float_input(0, 1, True)
    try:
        res, n = tailor_func(x, eps)
        print(f"Enter x: {x}")
        print(f"Enter eps: {eps}")
        print(f"MathFunc result = {math.log(1 + x)}")
        print(f"TailorFunc result = {res}")
        print(f"Number of iterations: {n}")
    except ValueError:
        print("Warning!!! Exception: ValueError")
    print("*" * 20)
    print(f"Enter to continue: ", end="")
    input()


def complete_task2():
    print("*"*20)
    print("Use auto generate? [y/n]")
    str_choose = input()
    amount = -1
    use_gen = False
    if str_choose == 'y' or str_choose == 'Y':
        use_gen = True
        print("How many numbers generate?")
        amount = int_input(0, 0, False)
    res = cycle(use_gen, amount)
    print(f"Amount of positive number: {res}")
    print("*"*20)
    print(f"Enter to continue: ", end="")
    input()


def complete_task3():
    print("*" * 20)
    print("Enter your string: ", end="")
    string = input()
    if is_hex(string):
        print("Your string is HEX number")
    else:
        print("Your string is NOT HEX number")
    print("*"*20)
    print(f"Enter to continue: ", end="")
    input()


def complete_task4():
    print("*" * 20)
    default_string = "o she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her"
    print("Use default string? [y/n]")
    choose = input()
    if not (choose == 'y' or choose == 'Y'):
        print("Enter your text: ")
        default_string = input()
    words_amount,  list_odd_words, min_word, repeated_words = text_analyze(default_string)
    print(f"Words amount: {words_amount}")
    print("Words with odd count of letters:")
    for word in list_odd_words:
        print(word, end=' ')
    print("\nThe shortest word begin at 'a': ", end="")
    if min_word == "":
        print("Not Found")
    else:
        print(min_word)
    print("Repeated words: ")
    for word in repeated_words:
        print(word, end=" ")
    print("")
    print("*" * 20)
    print(f"Enter to continue: ", end="")
    input()


def complete_task5():
    print("*" * 20)
    print("Enter a size of array: ")
    size = int_input(0, math.inf, True)
    float_list = list()
    print("Use auto generation? [y/n]")
    choose = input()
    if choose == 'y' or choose == 'Y':
        while size > 0:
            float_list.append(float(random.randint(-size, size)))
            size -= 1
    else:
        print("Enter list of float values: ")
        while size > 0:
            el = float_input(0, 0, False)
            float_list.append(el)
            size -= 15
    print("Resulted list: ")
    print(float_list)
    max_abs_el, res = list_analyze(float_list)
    print(f"Maximal absolute value: {max_abs_el}")
    print(f"Sum ending last positive number: {res}")
    print("*" * 20)
    print(f"Enter to continue: ", end="")
    input()
