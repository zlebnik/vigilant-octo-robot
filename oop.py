import math

# Есть N фигур, среди них может быть:
# 1. Круг - у него будет задан радиус
# 2. Прямоугольник - у него будут заданы 2 стороны
# Задача: вывести суммарную площадь всех фигур.
# Пример данных:

FIGURES = [
  {'type': 'round', 'params': [3]},
  {'type': 'rectangle', 'params': [3, 4]},
  {'type': 'rectangle', 'params': [4, 10]},
  {'type': 'round', 'params': [9]},
]

# Пример абстракции и инкапсуляции: класс Figure объявляет, что будет метод square, но не уточняет его реализацию
class Figure:
  def square(self) -> float:
    raise Exception('use subclass')


class Round(Figure):
  def __init__(self, radius):
    self.radius = radius
  
  def square(self) -> float:
    return math.pi * self.radius * self.radius


# Полиморфизм: реализация площади у прямоугольника отличается от таковой у круга
class Rectangle(Figure):
  def __init__(self, a, b):
    self.a = a
    self.b = b
  
  def square(self) -> float:
    return self.a * self.b


# Наследование: квадрат использует метод square родителя-прямоугольника
class Square(Rectangle):
  def __init__(self, a):
    super().__init__(a, a)


class FigureBuilder:
  def __init__(self):
    self.__builders = {}
  
  def add_builder(self, key, cls):
    self.__builders[key] = cls
  
  def build(self, key, args):
    return self.__builders[key](*args)

builder = FigureBuilder()
builder.add_builder('round', Round)
builder.add_builder('rectangle', Rectangle)

class FiguresList:
    def __init__(self, figures) -> None:
      self.figures: list[Figure] = []
      for f in figures:
        self.figures.append(builder.build(f['type'], f['params']))

    def square(self):
        return sum(f.square() for f in self.figures)


figures_list = FiguresList(FIGURES)

print(figures_list.square())