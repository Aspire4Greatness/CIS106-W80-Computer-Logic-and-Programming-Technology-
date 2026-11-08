tickets = int(input("How many tickets? "))

if tickets < 5:
    price = 75.00
else:
    if tickets <= 9:
        price = 70.00
    else:
        if tickets <= 24:
            price = 60.00
        else:
            price = 50.00

cost = price * tickets

print(f"Tickets     {tickets:>12}")
print(f"Price       ${price:>11.2f}")
print(f"Total cost  ${cost:>11.2f}")