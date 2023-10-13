animal_class = "mammal" or "reptile"
animal = input()

if animal == "dog":
    print("mammal")
elif animal == "crocodile" \
    or animal == "tortoise" \
    or animal == "snake":
    print("reptile")
else:
    print("unknown")

