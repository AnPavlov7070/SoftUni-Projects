# for h in range(24):
    # for m in range(60):
        # print(f"{h}:{m}")

hours = 0
while hours < 24:
    minutes = 0
    while minutes < 60:
        print(f"{hours}:{minutes}")
        minutes += 1
    hours += 1
