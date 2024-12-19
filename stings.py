# course = 'there's is the python course
# above method is not acceptable
# string are wrapped either into the single quotes or double quotes

course = "there's is the for the python course"
# print(course)

# but there is ''' '''  used to write for the multiple line of strings

code = ''' 
this 
is my 
multi line 
string
'''

# print(code)


# feature of python strings

name = 'Gaurav'
# print(name[0])  # G
# print(name[1])  # a
# print(name[-1])  # v
# print(name[1:])  # aurav

# copy strings

another = name[:]
# print(another) # Gaurav

test = 'jennifer'
# print(test[1:-1]) # ennife

# formating strings

first = 'gaurav'
last = 'chauhan'
full_name = f'{first} is already {last}'
print(full_name)

# methods of string in python

print(course.upper()) # THeres IS THE PYTHON COURSE
print(course.lower()) # there's is the python course
print(course.capitalize()) # There's is the python course
print(course.title()) # There's Is The Python Course
print(len(course))  # 36
print(course.find('p')) # 23
print(course.replace('is', 'are'))
print('this' in course) #false
print('This' in course) #true
