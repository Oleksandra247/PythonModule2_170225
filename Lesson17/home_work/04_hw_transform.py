# У вас есть список строк, некоторые из которых содержат email-адреса.
# Вам нужно извлечь все email-адреса и привести их к нижнему регистру.
# email-адреса содержат символ '@'.

log_entries = [
    "User logged in: john.doe@example.com",
    "Error occurred",
    "New user registered: Jane_Smith@Example.ORG",
    "Another log",
    "Contact us at support@test.co.uk"
]

e = []

for i in log_entries:
    if "@" in i:
        email = i.split(" ")[-1].lower()
        e.append(email)

print(e)
