import re

name_age = """
Animesh is 30 and Abhishek is 34
Supriti is 31 and Tanmoy is 33
"""

names = re.findall(r'[A-Z][a-z]*', name_age)  # returns a list with uppercase letters from name_age string
ages = re.findall(r'\d{1,3}', name_age)  # returns a list with 2 digit number from name_age string

age_dict = {}  # initialize an empty dictionary
x = 0
for each_name in names:
    age_dict[each_name] = ages[x]
    x += 1
print(age_dict)

# search work through regular expression

if re.search("inform", "We need to inform him on time"):
    print("Inform is there in the string")

# find all possible inform ord in a given string

find_inform = re.findall("inform", "We need to inform him with latest information")
for inform in find_inform:
    print(inform)
print(len(find_inform))

# print the starting and ending index of the matching string

str_regex = "We need to inform him with latest information"
for index in re.finditer("inform", str_regex):
    location = index.span()  # convert the index into a tuple
    print(location)

# Match word pattern with regexp

str_new = "Sat, hat, mat , pat"
all_str = re.findall('[Shmp]at', str_new)  # find all the patterns with S,h, m, p with "at"
for i in all_str:
    print(i)

range_str = re.findall('[h-m]at', str_new)  # include the range between h-m
for j in all_str:
    print(j)

range_str = re.findall('[^h-m]at', str_new)  # does not include the range between h-m
for j in all_str:
    print(j)
