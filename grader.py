# Student Grading System
name = input("Enter Student Name: ")
marks = float(input("Enter marks (0-100): "))

if marks >= 80:
    grade = "A+"
elif marks >= 70:
    grade = "A"
elif marks >= 60:
    grade = "B"
else:
    grade = "F"

print(f"Student: {name} | Marks: {marks} | Grade: {grade}")