def float_input(left, right, bound: bool = True) -> float:
    while True:
        try:
            res = float(input())
            if (res < left or res > right) and bound:
                print(f"Input number is bounding between {left} and {right}")
                print("Try again: ", end="")
            else:
                break
        except ValueError:
            print("This is not a float!")
            print("Try again: ", end="")
    return res


def int_input(left, right, bound: bool = True) -> int:
    while True:
        try:
            res = int(input())
            if (res < left or res > right) and bound:
                print(f"Input number is bounding between {left} and {right}")
                print("Try again: ", end="")
            else:
                break
        except ValueError:
            print("This is not a int!")
            print("Try again: ", end="")
    return int(res)
