# У вас есть список строк.
# Вам нужно получить список длин всех строк, которые имеют длину более 3 символов.

words = ["cat", "dog", "elephant", "mouse", "bird", "ant"]

l = list(filter(lambda x: len(x) > 3, words))
ln = list(map(len, l))

print(ln)
