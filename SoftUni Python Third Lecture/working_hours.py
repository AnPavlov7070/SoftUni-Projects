hour = int(input())
day = input()

if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
    if hour >= 10 and hour <= 18:
        print("open")
    else:
        print("closed")
else:
    print("closed")
