import math
import random
from CheckInput import int_input


def num_generator(amount):
    while amount > 0:
        yield random.randint(-9, 9)
        amount -= 1


def cycle(use_generator: bool, amount: int) -> int:
    """
    :param use_generator: determines whether generator will be used
    :param amount: amount of generated values
    :return:
    Result of sum all values
    """

    res = 0
    if use_generator:
        for i in num_generator(amount):
            print(i, end=" ")
            if i > 0:
                res += 1
        print("")
    else:
        print("Enter a sequence of numbers ended by 10 :")
        while True:
            num = int_input(0, 0, False)
            if num == 10:
                break
            if num > 0:
                res += 1
    return int(res)
