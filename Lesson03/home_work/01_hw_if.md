## "Шоколадка"

### Задание

![board.png](img/chocolat_lines.png)

Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек , если разрешается сделать один разлом
по прямой между дольками (то есть разломить шоколадку на два прямоугольника)

### Формат входных данных

Вводятся 3 целых положительных числа n, m и k. Точно известно, что k ≠ n ⋅ m.

### Формат выходных данных

Выведите "Да", если можно отломить от шоколадки ровно k долек, и "Нет" если нельзя.

### Решение задачи

```python
# TODO: you code here...
```

---
def can_break_chocolate(n, m, k):
    if k < n * m and (k % n == 0 or k % m == 0):
        return "Да"
    else:
        return "Нет"

# Ввод данных
n, m, k = map(int, input().split())

# Вывод результата
print(can_break_chocolate(n, m, k))

