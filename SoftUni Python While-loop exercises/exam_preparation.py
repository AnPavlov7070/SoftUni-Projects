command_at_end = "Enough"
border = 4

total_grades = 0
count_grades = 0
not_good_grades = 0


not_good_grades_count = int(input())

while True:
    command = input()
    if command == command_at_end:
        break

    last_problem_name = command
    problem_grade = int(input())
    total_grades += problem_grade
    count_grades += 1

    if problem_grade <= border:
        not_good_grades_count += 1
        if not_good_grades >= not_good_grades_count:
            break


avg_grade = total_grades / count_grades



