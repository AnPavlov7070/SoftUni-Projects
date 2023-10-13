groups_count = int(input())  # Въвеждаме броя на групите

musala_count = 0
monblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0

for _ in range(groups_count):
    group_size = int(input())  # Въвеждаме броя на хората в групата

    if group_size <= 5:
        musala_count += 1
    elif group_size <= 12:
        monblan_count += 1
    elif group_size <= 25:
        kilimanjaro_count += 1
    elif group_size <= 40:
        k2_count += 1
    else:
        everest_count += 1

total_count = musala_count + monblan_count + kilimanjaro_count + k2_count + everest_count

musala_percent = musala_count / total_count * 100
monblan_percent = monblan_count / total_count * 100
kilimanjaro_percent = kilimanjaro_count / total_count * 100
k2_percent = k2_count / total_count * 100
everest_percent = everest_count / total_count * 100

print(f"{musala_percent :.2f}%")
print(f"{monblan_percent :.2f}%")
print(f"{kilimanjaro_percent :.2f}%")
print(f"{k2_percent :.2f}%")
print(f"{everest_percent :.2f}%")