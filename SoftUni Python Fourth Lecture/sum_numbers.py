n = int(input())
sum_left = 0
for i in range(1, n + 1):
    sum_left = sum_left + int(input())

sum_right = 0

if sum_left == sum_right:
    print(sum_left)
else:
    diff = abs(sum_right - sum_left)
    print(diff)
