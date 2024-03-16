def is_hex(string: str) -> bool:
    """
    :param string: Input string
    :return: Checks is this string a HEX number
    """
    for el in string.lower():
        if el not in "0123456789abcdef":
            return False
    return True
