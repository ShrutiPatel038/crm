def final_price(price):
    if type(price) not in (int, float) or price < 0:
        raise ValueError("Invalid price")
    return round(price * 1.18, 2)
