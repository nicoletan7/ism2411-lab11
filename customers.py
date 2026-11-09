# REFLECTION

# 1. In real work, I would use .get() when I am not sure if a key exists
# because it prevents the program from crashing. I would use bracket notation
# when I know the key should exist and want an error if it is missing.


# EXERCISE 1

customer = {
    "name": "Alice",
    "email": "alice@email.com",
    "tier": "gold",
    "ytd_spend": 1250.00
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# EXERCISE 2

customer["phone"] = "555-123-4567"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)

# EXERCISE 3

email = customer.get("email", "no email on file")
print(email)
try:
    print(customer["email"])
except KeyError:
    print("KeyError: email not found")

# EXERCISE 4

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only gives the keys instead of both keys and values.
for key in customer:
    print(key)

# EXERCISE 5

tier_discounts = {
    "bronze": 0,
    "silver": .05,
    "gold": .10,
    "platinum": .15
}

discount_rate = tier_discounts.get(customer["tier"], 0)
purchase_price = 200
final_price = purchase_price * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount: {discount_rate:.0%}")
print(f"Final price: ${final_price:.2f}")


# EXERCISE 6

customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "silver"}
]

for person in customers:
    rate = tier_discounts.get(person["tier"], 0)
    discount_amount = 300 * rate
    print(
        f"{person['name']} - Tier: {person['tier']} - "
        f"Discount on $300: ${discount_amount:.2f}"
    )

# EXERCISE 7
catalog = {
    "Widget A": {
        "price": 9.99,
        "stock": 150
    },
    "Gadget C": {
        "price": 49.99,
        "stock": 8
    }
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product}")

# EXERCISE 8

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_by_region = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")