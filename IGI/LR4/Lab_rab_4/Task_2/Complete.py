import copy
import re
from zipfile import *


def complete_common(orig_text):
    print("English text: ")
    print(orig_text)
    text = orig_text.replace('\n', ' ')
    text += ' '
    sen_declarative = re.findall(r"[\w\s,:;’'\-\"(){}\[\]]+\. ", text)
    sen_interrogative = re.findall(r"[\w\s,:;’'\-\"(){}\[\]]+\? ", text)
    sen_exclamatory = re.findall(r"[\w\s,:;’'\-\"(){}\[\]]+! ", text)
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
    if len(words) == 0:
        print("Amount of words not be a zero number!")
        return False

    average_amount_of_letters = letters_amount//len(words)
    print(f"Average amount of letters in word: {average_amount_of_letters}")
    smiles = [smile[0] for smile in re.findall(r"([;:]-*(\(+|\)+|{+|}+|\[+|]+))", text)]
    print(f"Amount of smiles in text: {len(smiles)}")
    print(smiles)

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


def complete_individual(orig_text):
    text = orig_text.replace('\n', ' ') + ' '
    words = re.findall(r"[\w’'\-()_]*\w", text)
    print("Amount words in list: ")
    print(len(words))
    print(words)

    odd_words = list()
    for word in words:
        if len(word) % 2 == 1:
            odd_words.append(word)
    print("Words that have odd amount of symbols: ")
    print(odd_words)


    i_words = [w[0] for w in re.findall(r"(i[\w’'\-]*(\s|\. |\? |! ))", text)]
    min_i_word = "NOT FOUND                                                      "
    for i_word in i_words:
        if len(i_word) < len(min_i_word):
            min_i_word = i_word
    print(f"The smallest word that started by 'i': {min_i_word}")
    repeated_words = list()
    sort_words = sorted(words)
    sv_word = sort_words[0]
    count = 0
    for word in sort_words:
        if word == sv_word:
            count += 1
        else:
            if count > 1:
                repeated_words.append(sv_word)
            sv_word = word
            count = 1
    print("Repeated words:")
    print(repeated_words)
    # emails
    emails = re.findall(r"\w+@\w+\.\w+", text)
    destinations = [adr.split('@')[0] for adr in emails]
    print("Destinations and emails:")
    if len(emails) == 0:
        print("Not Found")
    else:
        print(emails)
        print(destinations)
    
    print("Modified text: ")
    new_text = re.sub(r"(\w)_\((\w)\)", r"\1[\2]", orig_text)
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

