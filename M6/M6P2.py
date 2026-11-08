partnum = int(input("Part number?"))
quantity = int(input("Quantity?"))
unitprice = 0.00

if partnum == 50 or partnum == 10:
    unitprice = 1.00
else:
    if partnum == 80 or partnum == 70:
        unitprice = 3.00
    else:
        if partnum == 99:
            unitprice = 2.00
        else:
            unitprice = 5.00
            
total = float(unitprice*quantity)

print(f"Part number     {partnum:>7}")
print(f"quantity        {quantity:>7}")
print(f"Unit price:    ${unitprice:>7.2f}")
print(f"Total price:   ${total:>7.2f}")







