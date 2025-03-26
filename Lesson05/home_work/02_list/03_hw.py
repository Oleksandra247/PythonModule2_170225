# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random

# создаём список из 10 случайных чисел от -100 до 100
numbers = []
for i in range(10):
    num = random.randint(-100, 100)
    numbers.append(num)

# считаем сумму положительных чисел, которые делятся на 2
summa = 0
for number in numbers:
    if number > 0 and number % 2 == 0:
        summa += number

print("Список:", numbers)
print("Сумма положительных чётных чисел:", summa)
