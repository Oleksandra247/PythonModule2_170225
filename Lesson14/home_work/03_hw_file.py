n = int(input("n: "))

with open("trykutnuk.txt", "w") as f:
    width = 2 * n - 1
    for i in range(1, n + 1):
        s = 2 * i - 1
        sp = (width - s) // 2
        l = ' ' * sp + '*' * s + '\n'
        f.write(l)