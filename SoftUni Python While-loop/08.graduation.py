name_of_the_student = input()
bad_result = 0
current_class = 1
grade_at_total = 0
while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        bad_result += 1
        if bad_result > 1:
            break
        continue
    current_class += 1
    grade_at_total += current_grade
if current_class <= 12:
    print(f"{name_of_the_student} has been excluded at {current_class} grade")
else:
    average_grade = grade_at_total / 12
    print(f"{name_of_the_student} graduated. Average grade: {average_grade:.2f}")

