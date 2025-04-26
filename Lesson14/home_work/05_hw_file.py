def read_workers(file_path="data/workers.txt"):
    workers = {}
    with open(file_path, encoding="utf-8") as file:
        next(file)
        for line in file:
            parts = line.strip().split()
            first_name, last_name = parts[0], parts[1]
            salary, position, hours_norm = int(parts[2]), parts[3], int(parts[4])
            workers[(first_name, last_name)] = {"salary": salary, "position": position, "hours_norm": hours_norm}
    return workers

def read_hours(file_path="data/hours_of.txt"):
    hours = {}
    with open(file_path, encoding="utf-8") as file:
        next(file)
        for line in file:
            parts = line.strip().split()
            first_name, last_name = parts[0], parts[1]
            worked_hours = int(parts[2])
            hours[(first_name, last_name)] = worked_hours
    return hours

workers = read_workers()
hours = read_hours()

def calculate(workers, hours):
    final_salaries = {}
    for key, info in workers.items():
        first_name, last_name = key
        norm = info["hours_norm"]
        base_salary = info["salary"]
        worked = hours.get((first_name, last_name), 0)

        if worked == norm:
            final_salary = base_salary
        elif worked < norm:
            final_salary = base_salary * (worked/norm)
        else:   
            overtime_hours = worked - norm
            overtime_pay = (base_salary / norm) * overtime_hours * 2
            final_salary = base_salary + overtime_pay
        final_salaries[f"{first_name} {last_name}"] = final_salary
    return final_salaries

salaries = calculate(workers, hours)
for name, salary in salaries.items():
    print(f"{name}: {salary}")