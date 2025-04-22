# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
  import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

x1, y1, r1 = 0, 0, 5
x2, y2, r2 = 0, 0, 3

distance = dist(x1, y1, x2, y2)

if distance + r2 <= r1:
    print("Вторая окружность целиком внутри первой")
elif distance + r1 <= r2:
    print("Первая окружность целиком внутри второй")
else:
    print("Окружности не вложены друг в друга")

# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
