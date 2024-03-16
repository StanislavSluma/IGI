def text_analyze(input_string: str):
    """
    :param input_string: Input text
    :return:
    amount_str - amount of words in text;
    list_even_str - list of words with even number letters;
    min_str - minimal words than begin at 'a' if not found empty string '';
    repeated_str - list of words that were repeated;
    """
    list_str = input_string.split(" ")
    list_str = [str(s).replace(',', '') for s in list_str]
    amount_str = len(list_str)
    list_even_str = filter(lambda s: len(str(s)) % 2 == 0, list_str)
    repeated_str = list()
    min = 1000
    min_str = ""

    for string in list_str:
        if len(string) >= 1:
            if string[0] == 'a' and len(string) < min:
                min_str = string
                min = len(min_str)

    for string in list_str:
        if list_str.count(string) > 1:
            if repeated_str.count(string) < 1:
                repeated_str.append(string)
    return amount_str, list_even_str, min_str, repeated_str
