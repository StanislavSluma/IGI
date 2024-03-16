from functools import reduce


def list_analyze(float_list: list):
    """
    :param float_list: list of float values
    :return:
    max_abs_el - maximal absolute value in list;
    res - sum of values up to last positive value;
    """
    max_abs_el = reduce(lambda x, y: x if abs(x) > abs(y) else y, float_list)
    float_list.reverse()
    unlock = False
    res = 0.0
    for el in float_list:
        if el > 0:
            unlock = True
        if unlock:
            res += el
    return max_abs_el, res
