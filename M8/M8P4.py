f = open("inventory.txt", "r")

sum = 0.00
count = 0

item = f.readline().rstrip('\n')

while item != "":
    qty = float(f.readline())
    price = float(f.readline())
    extended = qty * price

    print(f"item: {item}")
    print(f"quantity: {qty:,.0f}")
    print(f"price: ${price:,.2f}")
    print(f"extended price: ${extended:,.2f}\n")

    sum = sum + extended
    count = count + 1

    item = f.readline().rstrip('\n')

f.close()

print(f"total prices: ${sum:,.2f}")
print(f"orders: {count}")

if count > 0:
    average = sum / count
    print(f"average of orders: ${average:,.2f}")