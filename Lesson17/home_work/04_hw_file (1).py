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

def email(text):
    parts = text.split()
    for word in parts:
        if "@" in word:
            return word.strip(".,!:;?")
        
entries = filter(lambda l: "@" in l, log_entries)

e = list(map(email, entries))
print(e)