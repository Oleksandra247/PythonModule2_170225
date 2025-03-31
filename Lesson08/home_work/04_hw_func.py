# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def parse_fraction(f):
    space_index = f.index(" ")
    n = f[:space_index]  # целая часть
    num = ...  # числитель
    den = ...  # знаменатель

# TODO: your code here
def parse_fraction(f):
    space_index = f.index(" ")
    n = int(f[:space_index])  # целая часть
    fraction = f[space_index + 1:]
    num, den = map(int, fraction.split("/"))  # дробная часть
    return n, num, den

# пример использования
f1 = "2 4/5"
f2 = "1 1/3"

n1, num1, den1 = parse_fraction(f1)
n2, num2, den2 = parse_fraction(f2)

print("Первая дробь:")
print("Целая часть:", n1)
print("Числитель:", num1)
print("Знаменатель:", den1)

print("Вторая дробь:")
print("Целая часть:", n2)
print("Числитель:", num2)
print("Знаменатель:", den2)
