cont = input("execute program calculating interest? ").lower()

while cont == "yes":
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter interest rate: "))
    print()

    balance = principal
    totalInterest = 0.00
    year = 1

    print(f"{'Year':<6}{'Beginning':>14}{'Ending':>14}")
    print(f"{'':<6}{'Balance':>14}{'Balance':>14}")
    print()

    while year <= 5:
        beginning = balance
        interest = beginning * rate
        ending = beginning + interest

        print(f"{year:<6}{'$' + format(beginning, ',.2f'):>14}{'$' + format(ending, ',.2f'):>14}")

        totalInterest = totalInterest + interest
        balance = ending
        year = year + 1

    print()
    print(f"Total interest: ${totalInterest:,.2f}\n")

    cont = input("execute program again? ").lower()