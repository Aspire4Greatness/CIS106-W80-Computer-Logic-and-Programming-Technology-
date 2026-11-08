quantity = int(input("Enter quantity: "))

if quantity >= 1000:
    unitprice = 3.00
else:
    unitprice = 5.00

extendedprice = unitprice * quantity
tax = 0.07 * extendedprice
total = tax + extendedprice

print(f"Quantity: {quantity}")
print(f"Unit price: ${unitprice:.2f}")
print(f"Extended price: ${extendedprice:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")