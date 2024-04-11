import csv
import ast
import pickle


class Serializer:

    @staticmethod
    def serialize(filename, dictionary: dict):
        with open(filename, "w+", newline="") as file:
            columns = dictionary.keys()
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            writer.writerow(dictionary)

    @staticmethod
    def deserialize(filename):
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            new_dict = dict()
            for row in reader:
                for key in row:
                    new_dict[key] = ast.literal_eval(row[key])
        return new_dict

    @staticmethod
    def serialize_pickle(filename, dictionary):
        with open(filename, "wb+") as file:
            pickle.dump(dictionary, file)

    @staticmethod
    def deserialize_pickle(filename):
        with open(filename, "rb+") as file:
            return pickle.load(file)
