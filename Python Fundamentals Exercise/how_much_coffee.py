coffee_counter = 0

while True:
    event_logger = input()

    if event_logger == "END":
        break

    if event_logger.lower() in ["coding", "dog", "cat", "movie"]:
        if event_logger.islower():
            coffee_counter += 1
        else:
            coffee_counter += 2

if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)