floor_numbers = int(input())
room_numbers = int(input())
floor_letter = ""
for current_floor in range(floor_numbers, 0, -1):
    if current_floor == floor_numbers:
            floor_letter = "L"
    elif current_floor % 2 == 0:
            floor_letter = "O"
    else:
            floor_letter = "A"
    for current_room in range (room_numbers):
            print(f"{floor_letter}{current_floor}{current_room}", end = " ")
    print()



#number_of_floors = int(input())
#number_of_rooms = int(input())
#floor_letter = ""
#for current_floor in range(number_of_floors, 0, -1):
    #if current_floor == number_of_floors:
        #floor_letter = "L"
    #elif current_floor % 2 == 0:  # even floor
        #floor_letter = "O"
    #else:  # current floor % 2 != 0
        #floor_letter = "A"
    #for current_room in range(number_of_rooms):  # range(0, number_of_rooms)
        #print(f"{floor_letter}{current_floor}{current_room}", end = " ")
    #print()