f = open("employeeSalary.txt", "r")

totalBonus = 0.00

for i in range(5):
    name = f.readline().rstrip('\n')
    salary = float(f.readline())

    if salary >= 100000:
        rate = 0.20
    elif salary >= 50000:
        rate = 0.15
    else:
        rate = 0.10

    bonus = salary * rate

    print(f"Last name: {name}")
    print(f"Salary: ${salary:,.2f}")
    print(f"Bonus: ${bonus:,.2f}")
    print()
    totalBonus = totalBonus + bonus

f.close()

print(f"Total bonuses paid: ${totalBonus:,.2f}")