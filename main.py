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

def get_square(figure):
    if figure['type'] == 'round':
        return math.pi * figure['params'][0] * figure['params'][0]
    if figure['type'] == 'rectangle':
        return figure['params'][0] * figure['params'][1]

print(
    sum(
        map(
            get_square,
            FIGURES
        )
    )
)

result = 0
for f in FIGURES:
    result += get_square(f)
print(result)