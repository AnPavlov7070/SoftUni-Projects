total_presentation_sum = 0
presentation_sum = 0

judges_number = int(input())

command = input()
while not command == "Finish":
    current_presentation = command

    current_presentation_sum = 0
    for _ in range(judges_number):
        current_judges_score = float(input())
        current_presentation_sum += current_judges_score

    total_presentation_sum += current_presentation_sum
    presentation_sum += 1

    avg_score = current_presentation_sum / judges_number
    print(f"{current_presentation} - {avg_score :.2f}.")

    command = input()

avg_total_score = total_presentation_sum / (presentation_sum * judges_number)
print(f"Student's final assessment is {avg_total_score :.2f}.")
