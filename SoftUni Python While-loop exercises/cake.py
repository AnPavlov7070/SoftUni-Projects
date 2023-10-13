cake_width = int(input())
cake_length = int(input())

total_cake_pieces = cake_length * cake_width

cake_pieces_left = total_cake_pieces
while True:
    command = input()
    if command == "STOP":
        break

    current_pieces = int(command)
    cake_pieces_left -= current_pieces
    if cake_pieces_left <= 0:
        break

if cake_pieces_left > 0:
    print(f"{cake_pieces_left} pieces are left.")
else:
    print(f"No more cake left! You need {-cake_pieces_left} pieces more.")
