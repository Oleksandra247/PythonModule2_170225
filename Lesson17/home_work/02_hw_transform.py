# У вас есть список строк.
# Вам нужно получить список длин всех строк, которые имеют длину более 3 символов.

words = ["cat", "dog", "elephant", "mouse", "bird", "ant"]

lenghts = []
for i in words:
    if len(i) > 3:
        lenghts.append(len(i))

print(lenghts)
