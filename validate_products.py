from app import PRODUCTS

for p in PRODUCTS:
    assert p["name"] and p["price"] >= 0, "Invalid product"

print("All products are valid")
