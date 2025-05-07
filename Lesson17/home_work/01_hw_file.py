# У вас есть список цен товаров.
# Вам нужно применить скидку в 10% к каждому товару, цена которого превышает 100 единиц, и вывести новые цены.

def apply_discount(price):
    if price > 100:
        return price * 0.9
    return price

def apply_discounts(func, prices):
    return list(map(apply_discount, prices))

prices = [50, 120, 80, 150, 90, 200]

discount_prices = apply_discounts(apply_discount, prices)
print(discount_prices)
