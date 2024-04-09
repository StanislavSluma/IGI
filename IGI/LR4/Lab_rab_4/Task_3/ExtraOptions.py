from functools import reduce


class ExtraOptions:

    @staticmethod
    def average(collection: list):
        return reduce(lambda x, y: x + y, collection) / len(collection)

    @staticmethod
    def median(collection: list):
        sort_coll = sorted(collection)
        ln = len(sort_coll)
        if ln % 2 == 0:
            return (sort_coll[ln // 2 - 1] + sort_coll[ln // 2]) / 2
        else:
            return sort_coll[ln // 2]

    @staticmethod
    def moda(collection: list):
        diction = dict()
        max_val = 0
        for el in collection:
            if diction.get(el) != None:
                diction[el] += 1
                if diction[el] > max_val:
                    max_val = diction[el]
            else:
                diction[el] = 1
        modas = list()
        if max_val == 0:
            return modas
        for key in diction:
            if diction[key] == max_val:
                modas.append(key)
        return modas

    @staticmethod
    def dispersion(collection: list):
        av = ExtraOptions.average(collection)
        res = 0.0
        for el in collection:
            res += (el - av)**2
        return res / len(collection)

    @staticmethod
    def standard_deviation(collection: list):
        return ExtraOptions.dispersion(collection) ** (1/2)

