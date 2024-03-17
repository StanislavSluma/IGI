from Library import Library
from Serializer import Serializer


if __name__ == "__main__":
    library = Library()
    library.add_books("Pushkin", ["mama", "papa", "brat"])
    print(library.dict_lib)
    library.add_books("Pushkin", ["sestra", "pricol"])
    print(library.dict_lib)
    print(library.get_books("Pushkin"))
    #library.del_books("Pushkin", ["mama", "papa", "sestra", "sasatt"])
    print(library.dict_lib)
    library.add_books("Zhvakina", ["mama"])
    print(library.dict_lib)
    library.add_books("Zhvakina", ["suda"])
    print(library.dict_lib)
    #library.del_books("Zhvakina", ["suda", "tuda"])
    print(library.dict_lib)
    library.add_books("Chelovek", ["1","2","3","4"])
    library.add_books("Nechelovek", ["-1-", "-2-", "-3-", "-4-"])
    print(library.dict_lib)
    #Serializer.serialize("Library1.csv", library.dict_lib)
    library2 = Library(Serializer.deserialize("Library1.csv"))
    print(library2.dict_lib)
    Serializer.serialize_pickle("Library2.pickle", library.dict_lib)
    library3 = Library(Serializer.deserialize_pickle("Library2.pickle"))
    print(library3.dict_lib)

