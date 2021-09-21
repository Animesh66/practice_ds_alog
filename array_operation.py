from array import array

numbers = array("i", [25, 75, 15, 2, 95, 17, 25])
print(sorted(numbers))
print(numbers.count(25))
print(numbers.index(25))

tuple_new = (12, 34, 9)

for index, value in enumerate(tuple_new):
    print(index, value)

print(max(1,2))
print(min(3,4))
str = "I am a very bad boy"
str = str.split()[::-1]
print(str)
print(" ".join(reversed(str.split())))
