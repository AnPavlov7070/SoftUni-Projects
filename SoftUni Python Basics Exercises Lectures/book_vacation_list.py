number_of_pages = int(input())
pages_read_for_one_hour = int(input())
days_to_read = int(input())
time_needed_to_read_the_book = number_of_pages / pages_read_for_one_hour
hours_a_day_to_read = time_needed_to_read_the_book / days_to_read
print(int(hours_a_day_to_read))
