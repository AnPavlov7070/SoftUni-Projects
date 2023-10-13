#floats and numbers
num = 3
print(type(num))

num = 3.14
print(type(num))
# arithmetics
print(3 / 2)
print(3 + 2)
print(3 * 2)
print(3 - 2)
print(3 * (2 + 1))
print(3 * 2 + 1)
# 3 / 3
print(3 // 2)
# 3 * 3
print(3 ** 2)
print(3 % 2)
#multiply method
num = 1

num *= 10

print(num)
#zakruglqne = round method
print(round(2.75))
print(round(3.75, 1))

#comparison
num_1 = 3
num_2 = 2
print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)

num_3 = '100'
num_4 = '200'

num_3 = int(num_3)
num_4 = int(num_4)

print(num_3 + num_4)
# Lists, Tuples and sets
cources = ['History', 'Math', 'Geography', 'CompSci']

#adding item to the list
cources.append('Art')
cources.insert(0, 'Art')

print(len(cources))

#values = 'len' is for counting individual words inside ' '.
print(cources[0]) #this [] is called index.
print(cources[0:2])
print(cources[:2])
print(cources[2:])
print(cources)

#Extend method
cources_2 = ['Physics', 'Information Technology']

cources.insert(0, cources_2)
print(cources)

print(cources[0])

cources.extend(cources_2)
print(cources)

cources.append(cources_2)

#removing details
cources = ['History', 'Math', 'Geography', 'CompSci']

cources.remove('Math')
print(cources)

cources.pop()
print(cources)
popped = cources.pop()
print(popped)

#reverse list and sort
cources = ['History', 'Math', 'Geography', 'CompSci']
nums = [1, 5, 2, 4, 3]

cources.reverse()
print(cources)

cources.sort()
print(cources)

nums.sort()
print(nums)

nums.reverse()
print(nums)

sorted_cources = sorted(cources)
print(sorted_cources)

#printing minimal number
print(min(nums))
#printing the sum of all numbers
print(sum(nums))
#find index of a certain method
print(cources.index('CompSci'))

print(cources.index('Art'))

#check if something is in the list

print('Art' in cources)

