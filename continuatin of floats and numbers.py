courses = ['History', 'Math', 'Geography', 'CompSci']
print(courses)
# Looping Values

for index, course in enumerate(courses):
    print(index, course)
# start from num 1, not 0

for index, course in enumerate(courses, start=1):
    print(index, course)

#coma separate every item in the list

courses_str = ', '.join(courses)
print(courses_str)

#turning string back into a list

new_list = courses_str.split(' - ')
print(new_list)

# Changing Index Value

list_1 = ['History', 'Math', 'Geography', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

#Tuple = lists

tuple_1 = ['History', 'Math', 'Geography', 'CompSci']
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)

# Sets is the sam as tuple and lists, but it has {} bracelets

cs_courses = {'History', 'Math', 'Geography', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print('Math' in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))
#how to create empty lists, tuples and sets

empty_set = {}#This isn't right!
empty_set = set()




