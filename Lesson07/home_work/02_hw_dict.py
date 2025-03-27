# Данные о сотрудниках в программе хранятся в словаре
staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 47800
    },
]
# Вычислите:
print("Имя и Фамилию сотрудника с самой высокой зарплатой:")

# biggest = staff[0]
for person in staff:
    if person["salary"] > biggest["salary"]:
        biggest = person
print("Самая высокая зарплата у:", biggest["name"], biggest["surname"])TODO: your code here

print("Имя и Фамилию сотрудника с самой низкой зарплатой:")

# smallest = staff[0]
for person in staff:
    if person["salary"] < smallest["salary"]:
        smallest = person
print("Самая низкая зарплата у:", smallest["name"], smallest["surname"])TODO: your code here

print("Среднеарифметическую зарплату всех сотрудников")

# Ttotal = 0
for person in staff:
    total = total + person["salary"]
average = total / len(staff)
print("Средняя зарплата:", average)
ODO: your code here

print("Количество однофамильцев в организации")

#surnames = []
for person in staff:
    surnames.append(person["surname"])

count = 0
for surname in surnames:
    if surnames.count(surname) > 1:
        count += 1
print("Количество однофамильцев:", count)
 TODO: your code here

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")

#for i in range(len(staff)):
    for j in range(i + 1, len(staff)):
        if staff[i]["salary"] > staff[j]["salary"]:
            temp = staff[i]
            staff[i] = staff[j]
            staff[j] = temp

print("Сотрудники по зарплате (от меньшей к большей):")
for person in staff:
    print(person["name"], person["surname"]) TODO: your code here
