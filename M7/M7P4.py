cont = input("execute program calculating gross pay? ").lower()
responses = 0
totalPay = 0.00

while cont == "yes":
    name = input("last name? ")
    rate = float(input("hourly rate? "))
    hours = float(input("hours worked? "))
    print()

    if hours >= 40:
        hours = hours - 40
        gross = (hours*1.5*rate) + (rate * 40.00)
    else:
        gross = hours*rate
        
    print(f"Last name: {name}")
    print(f"Gross pay: {gross:.2f} \n")
    
    responses = responses + 1
    totalPay = gross + totalPay
    average = totalPay/responses
    
    cont = input("execute program again? ").lower()
    pass


print(f"Total gross is: {totalPay:.2f}")
print(f"Employee responses: {responses}")
print(f"Average pay is {average:.2f}\n")
