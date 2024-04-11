class ShapeColor:
    def __init__(self):
        self.__color = "blue"

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        if color.strip() in ["black", "grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]:
            self.__color = color
