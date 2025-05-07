# У вас есть список словарей, представляющих студентов с их именами и средними баллами.
# Вам нужно отфильтровать студентов, чей средний балл выше 4.5,
# и округлить средний балл оставшихся студентов до двух знаков после запятой.

students = [
    {'name': 'Alice', 'grade': 4.811111},
    {'name': 'Bob', 'grade': 3.9},
    {'name': 'Charlie', 'grade': 4.65222},
    {'name': 'David', 'grade': 4.2},
    {'name': 'Eve', 'grade': 4.9122222}
]

filtered = filter(lambda s: s["grade"] > 4.5, students)
rounded = map(lambda s: {"name": s["name"], "grade": round(s["grade"], 2)}, filtered)
print(list(rounded))