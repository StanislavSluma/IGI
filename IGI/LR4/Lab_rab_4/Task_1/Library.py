class Library:

    def __init__(self, dict_lib=dict()):
        self.__dict_lib = dict_lib.copy()

    @property
    def dict_lib(self):
        return self.__dict_lib

    # @dict_lib.setter
    # def dict_lib(self, dict):
    #     self.__dict_lib = dict.copy()

    def add_books(self, author_name, books: list):
        if self.__dict_lib.get(author_name, "not_found") == "not_found":
            self.__dict_lib[author_name] = books.copy()
        else:
            self.__dict_lib[author_name].extend(books)

    def del_books(self, author_name, books: list):
        if self.__dict_lib.get(author_name, "not_found") != "not_found":
            for book in books:
                try:
                    self.__dict_lib[author_name].remove(book)
                except ValueError:
                    continue

    def get_books(self, author_name, default=None):
        if self.__dict_lib.get(author_name, "not_found") != "not_found":
            return self.__dict_lib[author_name].copy()
        return default
