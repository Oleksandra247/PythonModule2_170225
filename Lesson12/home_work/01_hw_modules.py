
import math
import random

x1, y1 = random.randint(-10, 10), random.randint(-10, 10)
x2, y2 = random.randint(-10, 10), random.randint(-10, 10)
x3, y3 = random.randint(-10, 10), random.randint(-10, 10)

a = math.hypot(x2 - x1, y2 - y1)
b = math.hypot(x3 - x2, y3 - y2)
c = math.hypot(x1 - x3, y1 - y3)

p = (a + b + c)/2

s = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(s) "Вычисление площади случайного треугольника"
