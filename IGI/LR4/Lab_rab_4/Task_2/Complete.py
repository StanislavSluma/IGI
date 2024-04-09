import copy
import re
from zipfile import *


def complete_common(text):
    print("English text: ")
    print(text)
    sen_declarative = re.findall(r"[\w\s,:;’'\-\"()]+\.", text)
    sen_interrogative = re.findall(r"[\w\s,:;’'\-\"()]+\?", text)
    sen_exclamatory = re.findall(r"[\w\s,:;’'\-\"()]+!", text)
    count_decl = len(sen_declarative)
    count_inter = len(sen_interrogative)
    count_excl = len(sen_exclamatory)
    count_all = count_decl + count_inter + count_excl
    if count_all == 0:
        print("Amount of sentence not be a zero number!")
        return False
    print(f"Amount of sentence in text: {count_all}")
    print(f"Amount of declarative sentence in text: {count_decl}")
    #print(sen_declarative)
    print(f"Amount of interrogative sentence in text: {count_inter}")
    #print(res_interrogative)
    print(f"Amount of exclamatory sentence in text: {count_excl}")
    #print(res_exclamatory)
    words = re.findall(r"[\w’'\-]*\w", text)
    average_amount_of_words = len(words)//count_all
    print(f"Average amount of words in sentence: {average_amount_of_words}")
    letters_amount = 0
    for word in words:
        letters_amount += len(word)
    average_amount_of_letters = letters_amount//len(words)
    print(f"Average amount of letters in word: {average_amount_of_letters}")
    smiles = [smile[0] for smile in re.findall(r"([;:]-*(\(+|\)+|{+|}+|\[+|]+))", text)]
    print(f"Amount of smiles in text: {len(smiles)}")

    #print(smiles)

    # with open("Task_2/save_task2.txt", "w") as file:
    #     file.write(f"Amount of sentence in text: {count_all}\n")
    #     file.write(f"Amount of declarative sentence in text: {count_decl}\n")
    #     file.write(f"Amount of interrogative sentence in text: {count_inter}\n")
    #     file.write(f"Amount of exclamatory sentence in text: {count_excl}\n")
    #     file.write(f"Average amount of words in sentence: {average_amount_of_words}\n")
    #     file.write(f"Average amount of letters in word: {average_amount_of_letters}\n")
    #     file.write(f"Amount of smiles in text: {len(smiles)}\n")
    return True


def complete_individual(text):

    words = re.findall(r"[\w’'\-]*\w", text)
    print("All words in list: ")
    print(words)

    less_than_7 = 0
    for word in words:
        if len(word) < 7:
            less_than_7 += 1
    print(f"Amount of words that less than 7 symbols: {less_than_7}")


    a_words = [w[0] for w in re.findall(r"([\w’'\-]+a(\s|\.|\?|!))", text)]
    min_a_word = "NOT FOUND                                                      "
    for a_word in a_words:
        if len(a_word) < len(min_a_word):
            min_a_word = a_word
    print(f"The smallest word that ended by 'a': {min_a_word}")

    new_words = sorted(words, key=lambda word: -1 * len(word))
    print(new_words)

    print("Modified text: ")
    new_text = re.sub(r"([a-z][A-Z])", r"_?_\1_?_", text)
    print(new_text)
    with open("Task_2/save_task2.txt", "w") as file:
        file.write(new_text)

    with ZipFile("Task_2/zipfile_task2.zip", "w") as myzip:
        with myzip.open("modified_text.txt", "w") as file:
            encoded_str = bytes(new_text, "UTF-8")
            file.write(encoded_str)

    print("ZipInfo: ")
    with ZipFile("Task_2/zipfile_task2.zip", "r") as myzip:
        for item in myzip.infolist():
            print(f"File Name: {item.filename} Date: {item.date_time} Size: {item.file_size}")


def complete_task2():
    ch = input("Use individual or default text? [i/d]\n")
    if ch.lower() == "i":
        text = input("Enter a text please: ")
        if complete_common(copy.copy(text)):
            complete_individual(text)
    else:
        with open("Task_2/text_task2.txt", "r") as file:
            text = file.read()
        if complete_common(copy.copy(text)):
            complete_individual(text)
    input("Enter to continue...")

