## "Таблица умножение"

### Задание

Требуется вывести на экран двумерную таблицу умножения от 1 до n.

### Формат входных данных

Дано целое положительное число n. 1 < n < 9

### Формат выходных данных

Вывести таблицу умножения. Смотри пример.\
Если знаете как, выравняйте выводимые значения как в примере.

#### Пример
```
Входные данные
n = 5
Выходные данные
1  2  3  4  5  
2  4  6  8 10 
3  6  9 12 15 
4  8 12 16 20 
5 10 15 20 25
```

### Решение задачи

```python
# TODO: you code here...
```

---

<details>
<summary>Подсказка-1</summary>
Для решения задачи вам понадобятся вложенные циклы.

```python
while ...:  # внешний цикл
    while ...:  # внутренний цикл
        ...
```
Внешний цикл будет перебирать числа из диапазона [1, n], а внутренний выводить строку для каждого числа диапазона.
</details>

<details>
<summary>Подсказка-2</summary>
Чтобы выводить значение print'ами на одной строке, используйте:

```python
print(1, end=" ")
print(2, end=" ")
print(3, end=" ")
...
```
</details>
# Входные данные
n = 5

# Внешний цикл — по строкам
i = 1
while i <= n:
    # Внутренний цикл — по столбцам
    j = 1
    while j <= n:
        print(f"{i * j:3}", end=" ")
        j += 1
    print()  # Переход на новую строку
    i += 1
