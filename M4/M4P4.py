first_name = input("First name: ").title()
steps = int(input("Steps walked (whole numbers only pls): "))

calories_burned = steps * 0.25

print()
print(f"First name: {first_name}")
print(f"Calories burned: {calories_burned:.2f}")