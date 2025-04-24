# "Моделирование случайного леса"
# Создайте функцию, которая генерирует случайный "лес" в виде двумерного массива.
# Каждая ячейка массива должна представлять собой либо "дерево", либо "пустое пространство".
# Используйте random.random() для определения, будет ли в ячейке дерево или нет.
# Визуализируйте сгенерированный лес, например, выводя символы "T" для деревьев и "." для пустых пространств.
import random

def generate_forest(rows: int, columns: int) -> list:
    forest = []
    for i in range(rows):
        line = [random.choice([".", "T"]) for i in range(columns)]
        forest.append(line)
    return forest


forest = generate_forest(10, 10)

for line in forest:
    print(" ".join(line))
