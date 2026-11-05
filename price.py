def final_price(price, tax=18):
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("Invalid price")
    return round(price + price * tax / 100, 2)
