from app import PRODUCTS

def validate(product):
    return product["name"] != "" and product["price"] >= 0

for p in PRODUCTS:
    assert validate(p), f"Invalid product: {p}"
    print("Valid:", p["name"])

print("All products are valid")
