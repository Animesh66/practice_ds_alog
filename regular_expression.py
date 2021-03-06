import re

name_age = """
Animesh is 30 and Abhishek is 34
Supriti is 31 and Tanmoy is 33
"""

names = re.findall(r'[A-Z][a-z]*', name_age)  # returns a list which starts with uppercase letters followed by
# lowercase letters from name_age string
ages = re.findall(r'\d{2}', name_age)  # returns a list with 2 digit number from name_age string

age_dict = {}  # initialize an empty dictionary
x = 0
for each_name in names:
    age_dict[each_name] = ages[x]
    x += 1
print(age_dict)

# search work through regular expression

if re.search("inform", "We need to inform him on time"):
    print("Inform is there in the string")

# find all possible inform word in a given string

find_inform = re.findall("inform", "We need to inform him with latest information")
for inform in find_inform:
    print(inform)
print(len(find_inform))

# print the starting and ending index of the matching string

str_regex = "We need to inform him with latest information"
for index in re.finditer("inform", str_regex):
    location = index.span()  # convert the start and finish index of the matched string into a tuple
    print(location)

# Match word pattern with regexp

str_new = "sat, hat, mat , pat"
all_str = re.findall('[shmp]at', str_new)  # find all the patterns with S,h, m, p with "at" in the end
for i in all_str:
    print(i)

range_str = re.findall('[h-m]at', str_new)  # include the range between h-m
for j in all_str:
    print(j)

range_str = re.findall('[^h-m]at', str_new)  # does not include the range between h-m
for j in all_str:
    print(j)

# replace character in string

food = "hat rat mat pat"
regex = re.compile(r"[r]at")  # re.compile() can combine a regular expression pattern into pattern objects,
# which can be used for pattern matching. It also helps to search a pattern again without rewriting it.
food = regex.sub("food", food)
print(food)

# print 2 backslashes

rand_str = "here is \\drogba"
print(re.search(r"\\drogba", rand_str))

# find digits using regex

num = "123 1234 12345 123456 1234567"
print("Matches: ", re.findall(r"\d{5,7}", num))

# Validate phone number

# \w means [A-Za-z0-9_]
# \W means [^A-Za-z0-9_]
# \s means white-space

phn_no = "412-555-1212"

if re.search(r"\w{3}-\w{3}-\w{4}", phn_no):
    print("it is a phone number")

# Validate fullname

first_name = "Animesh Mukherjee"
if re.search(r"\w{2,20}\s\w{2,20}", first_name):
    print("Valid fullname")

# Validate email id

email = """
    animesh5678@gmail.com, 
    fuck_you@email.com, mylove@.com, 
    supriti_.&&12%@gmail.com.au, 
    makafee@dk@com.au, 
    san@gmail.com, 
    slkop@@sk.com.au, 
    amit_2013+$$@email.co.in
"""
valid_email = re.findall(r"[\w.%+-]{1,20}[@]{1}[\w.-]{2,20}[.]{1}[A-Za-z]{2,3}", email)
print("Email matches: ", len(valid_email))
for ve in valid_email:
    print(f"{ve} is a valid email")
