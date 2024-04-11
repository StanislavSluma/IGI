from Task_1.Library import Library
from Task_1.Serializer import Serializer
from Checkinput import *


def complete_task1():
    try:
        library = Serializer.deserialize_pickle("Task_1/Library.pickle")
    except BaseException:
        library = Library()
        Serializer.serialize_pickle("Task_1/Library.pickle", library)

    print("Wellcome to library!")
    print("Enter a number, please\n")
    while True:
        print("0 >> exit")
        print("1 >> Add book")
        print("2 >> Delete book")
        print("3 >> Find author")
        print("4 >> Print all library")
        choose = input()
        if choose == "0":
            Serializer.serialize_pickle("Task_1/Library.pickle", library)
            Serializer.serialize("Task_1/Library.csv", library.dict_lib)
            break
        elif choose == "1":
            author = input("Enter a author name: ")
            print("How many books you want to added: ", end="")
            cycle = int_input(1, 10)
            books = list()
            while cycle > 0:
                books.append(input("Enter a book name: "))
                cycle -= 1
            library.add_books(author, books)
            input("Enter to continue...")
        elif choose == "2":
            author = input("Enter a author name: ")
            print("How many books you want to deleted: ", end="")  # do a check
            cycle = int_input(1, 10)
            books = list()
            while cycle > 0:
                books.append(input("Enter a book name: "))
                cycle -= 1
            library.del_books(author, books)
            input("Enter to continue...")
        elif choose == "3":
            author = input("Enter a author name: ")
            books = library.get_books(author, default="NF")
            print("Result: ")
            if books == "NF":
                print("This author not found!")
            else:
                for book in books:
                    print(book, end=" ")
                print()
            input("Enter to continue...")
        elif choose == "4":
            print(library.dict_lib)
            input("Enter to continue...")
        else:
            print("Enter only 0, 1, 2, 3, 4!")
            input("Enter to continue...")

