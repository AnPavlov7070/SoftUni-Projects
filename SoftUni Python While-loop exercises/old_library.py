checked_books = 0

targeted_book = input()
current_book = input()
while current_book != "No More Books":
    if current_book == targeted_book:
        break

    checked_books += 1
    current_book = input()
if current_book != "No More Books":
    print(f"You checked {checked_books} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {checked_books} books.")