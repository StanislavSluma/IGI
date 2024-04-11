class ShapeNameMixin:

    def get_name(self):
        if self.__name:
            return self.__name
        else:
            return "default"

    def set_name(self, name: str):
        self.__name = name
