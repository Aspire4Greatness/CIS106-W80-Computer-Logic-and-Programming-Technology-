cont = input("execute program calculating discount? ").lower()

discountSum = 0

while cont == "yes":
    quantity = int(input("quantity? "))
    price = float(input("Price? "))
    extended = price * quantity
    print()

    if extended > 10000:
        discount = .25
    else:
        discount = .10
    amountOff = extended * discount
    total = extended - amountOff
    
    print(f"extended price: ${extended:.2f}")
    print(f"discount amount: ${amountOff:.2f}")
    print(f"total price: ${total:.2f}")
    
    discountSum = amountOff + discountSum
    
    
    cont = input("execute program again? ").lower()
    pass


print(f"Total discount given: ${discountSum:.2f}")
