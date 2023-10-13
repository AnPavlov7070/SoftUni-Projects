while True:
    name = input()

    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break

    elif name == "Voldemort":
        print("You must not speak of that name!")
        break

    length = len(name)
    if length < 5:
        print(f"{name} goes to Gryffindor.")
    elif length == 5:
        print(f"{name} goes to Slytherin.")
    elif length == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")






