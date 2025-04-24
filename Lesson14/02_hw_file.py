summa = 0
with open("data/info.txt", "r") as f:
    for line in f:
        try:
            summa += int(line.strip())
        except ValueError:
            pass

print(summa)
