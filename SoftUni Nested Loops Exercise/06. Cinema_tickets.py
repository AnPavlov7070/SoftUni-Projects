total_tickets = 0
kids_total = 0
standard_total = 0
students_total = 0



command = input()
while not command == "Finish":
    current_movie = input()
    total_seats = int(input())
    free_seats = total_seats





   while free_seats > 0:
       current_ticket_type = input()

       if current_ticket_type == "End":
           break

       free_seats -= 1
       if current_ticket_type == "student":
           pass
       elif current_ticket_type == "standard":
           pass
       elif current_ticket_type == "kid":
           pass



percent_students = students_total / total_tickets * 100
percent_standard = standard_total / total_tickets * 100
percent_kids = kids_total / total_tickets * 100


print(f"Total tickets: {total_tickets}")
print(f"{percent_students :.2f}% student tickets.")
print(f"{percent_standard :.2f} standard tickets.")
print(f"{percent_kids :.2f} kids tickets.")







    command = input()