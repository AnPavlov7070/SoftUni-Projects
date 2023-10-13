students_at_the_exam = int(input())

top_students = 0
all_at_4 = 0
all_at_3 = 0
failed_students = 0
sum_total_grade = 0

for _ in range(students_at_the_exam):
    grade = float(input())
    sum_total_grade += grade

    if grade >= 5.00:
        top_students += 1
    elif 4.00 <= grade <= 4.99:
        all_at_4 += 1
    elif 3.00 <= grade <= 3.99:
        all_at_3 += 1
    else:
        failed_students += 1

percentage_top_students = (top_students / students_at_the_exam) * 100
percentage_all_at_4 = (all_at_4 / students_at_the_exam) * 100
percentage_all_at_3 = (all_at_3 / students_at_the_exam) * 100
percentage_failed_students = (failed_students / students_at_the_exam) * 100
grade_average = sum_total_grade / students_at_the_exam

print(f"Top students: {percentage_top_students:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_all_at_4:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_all_at_3:.2f}%")
print(f"Fail: {percentage_failed_students:.2f}%")
print(f"Average: {grade_average:.2f}")

