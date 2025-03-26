# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]
import math

input_list = [2, -5, 8, 9, -25, 25, 4]
output_list = []

for num in input_list:
    if num >= 0:
        root = math.sqrt(num)
        if root.is_integer():
            output_list.append(int(root))

print(output_list)
