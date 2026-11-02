# -*- coding: utf-8 -*-
last_name = input("Enter student last name: ")
last_name = last_name.title()
midterm = float(input("Enter midterm exam score (0-100): "))
final_exam = float(input("Enter final exam score (0-100): "))

total_exam_points = (midterm * 0.40) + (final_exam * 0.60)

print("\n")
print(f"Student last name: {last_name}")
print(f"Total exam points: {total_exam_points:.2f}")