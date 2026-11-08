books = int(input("Enter number of books: "))
cost = float(input("Enter cost per book: "))

total = cost * books

if total > 50:
    shipping = 0
else:
    shipping = 25

print(f"Total: ${total:.2f}")
print(f"Shipping: ${shipping:.2f}")