student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}
for key, value in student_scores.items():
    if value <= 70:
        value = "Fail"
    elif value <= 80:
        value = "Acceptable"
    elif value <= 90:
        value = "Exceeds Expectations"
    elif value < 100: # or just else
        value = "Outstanding"
    student_grades[key] = value

print(student_grades)

#Solución profesora:
""" for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades) """