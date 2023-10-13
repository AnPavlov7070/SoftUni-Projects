Instagram_fine = 100
Facebook_fine = 150
Reddit_fine = 50

opened_tabs = int(input())
salary = float(input())

for i in range(opened_tabs):
    current_opened_tab = input()

    if current_opened_tab == "Facebook":
        salary -= Facebook_fine


    elif current_opened_tab == "Instagram":
        salary -= Instagram_fine


    elif current_opened_tab == "Reddit":
        salary -= Reddit_fine

    if salary <= 0:
        break

if salary > 0:
    print(f"{int(salary)}")
else:
    print("You have lost all your salary.")

