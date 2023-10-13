import sys

max_num = -sys.maxsize
num_sum = 0

n = int(input())

for k in range(n):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num

        num_sum += current_num

rest_sum = num_sum - max_num
if max_num == rest_sum:
    print(f"Yes")
    print(f"Sum= {num_sum}")
else:
    print("No")
    num_sum = num_sum - max_num
    print(f"Diff={abs(max_num - num_sum)}")
