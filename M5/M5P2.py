item = input("Enter item (A or B): ")
quantity = int(input("Enter quantity: "))

if item == "A":
    price = 10.00
else:
    price = 20.00

total = price * quantity

print(f"Item: {item}")
print(f"Unit price: ${price:.2f}")
print(f"Total: ${total:.2f}")