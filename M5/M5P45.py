name = input("What's your name?")
deps = int(input("How many dependants?"))
gross = float(input("Gross income?"))

adjgross = gross - (deps*12000)

if adjgross > 50000:
    inctax = .2*adjgross
else:
    inctax = .1*adjgross
    
if adjgross<0:
    inctax = 100

print(f"Last name: {name}")
print(f"Gross income: ${gross:.2f}")
print(f"Dependants: {deps}")
print(f"Adjiusted gross income: ${adjgross:.2f}")
print(f"Income tax: ${inctax:.2f}")

