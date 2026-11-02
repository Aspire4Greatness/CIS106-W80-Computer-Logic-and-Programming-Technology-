purchase_price = float(input("Enter the purchase price per share: "))
current_price = float(input("Enter the current stock price: "))
quantity = float(input("Enter the quantity of stock: "))

net_change = (current_price - purchase_price) * quantity

print()
print(f"Net value: ${net_change:.2f}")