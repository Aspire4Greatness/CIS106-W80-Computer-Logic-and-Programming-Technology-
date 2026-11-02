make = input("Make of car?\n")
model = input("Model of car?\n")
msrp = float(input("MSRP of car?\n"))
discount_percent = float(input("Discount percent on car (in decimal)?\n"))


amount_off = (msrp * discount_percent)
discounted_price = msrp - amount_off

print(f"Make: {make} \nModel: {model} \nMSRP: ${msrp} \nDiscount percent (decimal): {discount_percent} \n")
print(f"Amount off: ${amount_off:.2f}")
print(f"Discounted Price: ${discounted_price:.2f}")