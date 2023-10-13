import sys

# number_max = 0
number_min = sys.maxsize
command = input()
while command != "Stop":
     current_NUMBER = int(command)
     if current_NUMBER < number_min:
         number_min = current_NUMBER
     command = input()
print(number_min)