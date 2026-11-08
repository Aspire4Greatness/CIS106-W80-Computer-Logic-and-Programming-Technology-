quantity = int(input("Enter quantity of widgets: "))

if quantity < 5000:
    price = 30.00
else:
    if quantity < 10000:
        price = 20.00
    else:
        price = 10.00

extprice = (price * quantity)
tax = extprice * 0.07
total = tax + extprice



print(f"Extended Price   ${extprice:>12.2f}")
print(f"Tax              ${tax:>12.2f}")
print(f"Total            ${total:>12.2f}")