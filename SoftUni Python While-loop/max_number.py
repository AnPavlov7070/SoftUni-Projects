import sys

# number_max = 0
number_max = - sys.maxsize
command = input()
while command != "Stop":
     current_NUMBER = int(command)
     if current_NUMBER > number_max:
         number_max = current_NUMBER
     command = input()
print(number_max)