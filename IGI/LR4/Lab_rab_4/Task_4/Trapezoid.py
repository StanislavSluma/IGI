from Task_4.Shape import Shape
from Task_4.ShapeColor import ShapeColor
from Task_4.ShapeMixin import ShapeNameMixin


class Trapezoid(Shape, ShapeNameMixin):
    __base_name = 'base trapezoid'

    def __init__(self, a=1.0, b=1.0, h=1.0, shape_color: ShapeColor = ShapeColor()):
        if a <= 0.0 or b <= 0.0 or h <= 0.0:
            self.__a = 1.0
            self.__b = 1.0
            self.__h = 1.0
        else:
            self.__a = a
            self.__b = b
            self.__h = h
        self.set_name(self.__base_name)
        self.__shape_color = shape_color

    def set_params(self, a, b, h):
        if not (a <= 0.0 or b <= 0.0 or h <= 0.0):
            self.__a = a
            self.__b = b
            self.__h = h

    def get_params(self):
        return self.__a, self.__b, self.__h

    def set_color(self, color: str):
        self.__shape_color.color = color

    def get_color(self):
        return self.__shape_color.color

    def area(self):
        return (self.__a + self.__b) / 2 * self.__h

    def get_points(self):
        points = list()
        #normalize = 1 / max(self.__a, self.__b, self.__h)
        normalize = 1
        points.extend([(0.0, 0.0), (self.__b * normalize, 0.0)])
        points.extend([(points[1][0] / 2 + self.__a * normalize / 2, self.__h * normalize),
                       (points[1][0] / 2 - self.__a * normalize / 2, self.__h * normalize)])
        return points

    def __str__(self):
        return ("Name: {}, a: {}, b: {}, h: {}, color: {}"
                .format(self.get_name(), self.__a, self.__b, self.__h, self.__shape_color.color))
