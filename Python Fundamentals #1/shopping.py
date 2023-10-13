budget = int(input())
counter = input()

while counter != "End":
    price_of_product = int(counter)
    budget -= price_of_product
    if budget < 0:
        print("You went in overdraft!")
        break
    counter = input()
else:
    print("You bought everything needed.")
