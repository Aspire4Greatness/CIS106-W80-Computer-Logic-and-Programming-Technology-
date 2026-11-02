fixed_costs = float(input("Enter the fixed costs: "))
price_per_unit = float(input("Enter the price per unit: "))
cost_per_unit = float(input("Enter the cost per unit: "))

break_even = fixed_costs / (price_per_unit - cost_per_unit)
break_even_units= int(break_even + .9)

print()
print(f"To break even exactly: {break_even} items sold")
print(f"To break even realistically: {break_even_units} items sold")
