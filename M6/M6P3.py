principal = float(input("what is the principal amount: "))
year = int(input("what are the years to maturity: "))

# Principle                   Years to Maturity    Interest Rate
# >$100,000                        5                    6%
# $50,000 to $100,000             10                    5%
# $50,000 to $100,000              5                    4%
# Any other principle        any other years            2%


if year == 5:
    if principal > 100000:
        interest = 0.06
    else:
        if principal >= 50000:
            interest = 0.04
        else:
            interest = 0.02
else:
    if year == 10:
        if principal >= 50000:
            if principal <= 100000:
                interest = 0.05
            else:
                interest = 0.02
        else:
            interest = 0.02
    else:
        interest = 0.02

fyi = principal * interest

print(f"Principal            ${principal:>12.2f}")
print(f"Interest rate (%)     {interest * 100:>12.2f}")
print(f"Interest amount      ${fyi:>12.2f}")