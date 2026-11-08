name = input("Enter appliance name: ")
cost = float(input("Enter appliance cost: "))

if cost > 1000:
    warranty = 0.1 * cost
else:
    warranty = 0.05 * cost

total = warranty + cost

print(f"Name: {name}")
print(f"Cost: ${cost:.2f}")
print(f"Warranty cost: ${warranty:.2f}")
print(f"Total: ${total:.2f}")