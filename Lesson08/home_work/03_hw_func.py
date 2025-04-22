# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def lucky_ticket(ticket_number):
    str_ticket = str(ticket_number)
    if len(str_ticket) != 6:
        return False
    
    frst = int([0]str_ticket) + int(str_ticket[1]) + int(str_ticket[2])
    last = int(str_ticket[3]) + int(str_ticket[4]) + int(str_ticket[5])

    return frst == last


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751)) 
