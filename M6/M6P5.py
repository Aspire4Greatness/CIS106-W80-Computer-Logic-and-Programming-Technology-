name = input("Employee last name? ")
salary = float(input("Salary? "))
level = int(input("Job level? "))

if level < 5:
    bonusRate = 0.10
else:
    if level < 10:
        bonusRate = 0.20
    else:
        bonusRate = 0.25

bonus = salary * bonusRate

print(f"Name           {name:>12}")
print(f"Bonus amount  ${bonus:>12.2f}")