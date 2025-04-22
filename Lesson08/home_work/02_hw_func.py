# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
 import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

xa, ya = 1, 1
xb, yb = 3, 3
xc, yc = 2, 1

ab = distance(xa, ya, xb, yb)
bc = distance(xb, yb, xc, yc)
ac = distance(xa, ya, xc, yc)

short = min(ab, bc, ac)
if short == ab:
    segment = "AB"
elif short == bc:
    segment = "BC"
else:
    segment = "AC"


print("Самый короткий отрезок:", segment)  


print("Самый короткий отрезок:", ...)  # Выводим название отрезка, например “АС”.
