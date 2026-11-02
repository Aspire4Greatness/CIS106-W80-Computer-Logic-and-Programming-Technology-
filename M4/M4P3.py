meal_total = float(input("Enter the total for the meal: "))

tip_15 = meal_total * 0.15
tip_18 = meal_total * 0.18
tip_20 = meal_total * 0.20

total_15 = meal_total + tip_15
total_18 = meal_total + tip_18
total_20 = meal_total + tip_20

print()
print("With 15% Tip:")
print()
print("Total:".ljust(14) + f"{meal_total:.2f}".rjust(8))
print("Tip:".ljust(14) + f"{tip_15:.2f}".rjust(8))
print("Total with Tip".ljust(14) + f"{total_15:.2f}".rjust(8))
print()
print()
print("With 18% Tip:")
print()
print("Total:".ljust(14) + f"{meal_total:.2f}".rjust(8))
print("Tip:".ljust(14) + f"{tip_18:.2f}".rjust(8))
print("Total with Tip".ljust(14) + f"{total_18:.2f}".rjust(8))
print()
print()
print("With 20% Tip:")
print()
print("Total:".ljust(14) + f"{meal_total:.2f}".rjust(8))
print("Tip:".ljust(14) + f"{tip_20:.2f}".rjust(8))
print("Total with Tip".ljust(14) + f"{total_20:.2f}".rjust(8))