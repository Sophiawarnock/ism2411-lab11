# ISM2411 Lab 11 - Customer Dictionary & Lookup
# Name: Sophia Warnock

# EXERCISE 1 - One customer

customer = {
    "name": "Alice",
    "email": "alice@email.com",
    "tier": "gold",
    "ytd_spend": 500
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# EXERCISE 2 - Update and add

customer["phone"] = "555-1234"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# EXERCISE 3 - Safe lookup

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")

# EXERCISE 4 - Iterate

for key, value in customer.items():
    print(f"{key}: {value}")

# Loop without .items()
for key in customer:
    print(key)

# EXERCISE 5 - Lookup table

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]

discount_rate = tier_discounts.get(tier, 0)

price = 200

final_price = price * (1 - discount_rate)

print("Tier:", tier)
print("Discount:", discount_rate)
print("Final price:", final_price)

# EXERCISE 6 - List of dictionaries

customer1 = {
    "name": "Alice",
    "tier": "bronze"
}

customer2 = {
    "name": "Bob",
    "tier": "silver"
}

customer3 = {
    "name": "Charlie",
    "tier": "gold"
}

customers = [customer1, customer2, customer3]

for person in customers:
    tier = person["tier"]
    rate = tier_discounts.get(tier, 0)
    discount = 300 * rate

    print(f"{person['name']}: {tier}, discount ${discount:.2f}")

# EXERCISE 7 - Nested catalog

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
        print(product, "LOW STOCK")

# EXERCISE 8 - Sales by region

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    summary[region] = summary.get(region, 0) + amount

for region in sorted(summary):
    print(region, summary[region])