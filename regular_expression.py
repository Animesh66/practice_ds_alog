import re

name_age = """
Animesh is 30 and Abhishek is 34
Supriti is 31 and Tanmoy is 33
"""

names = re.findall(r'[A-Z][a-z]*]', name_age)  # returns a list with uppercase letters from name_age string
ages = re.findall(r'\d{1,3}', name_age)  # returns a list with 2 digit number from name_age string

age_dict = {}  # initialize an empty dictionary
x = 0
for each_name in names:
    age_dict[each_name] = ages[x]
    x += 1
print(age_dict)


