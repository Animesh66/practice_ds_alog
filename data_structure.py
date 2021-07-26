expense = [2200, 2350, 2600, 2130, 2190]

print("In Feb, how many dollars you spent extra compare to January: ", expense[1] - expense[0])
print("Find out your total expense in first quarter (first three months) of the year: ",
      expense[0] + expense[1] + expense[1])
# Find out if you spent exactly 2000 dollars in any month
for index, exp in enumerate(expense):
    if exp == 2000:
        print("Expense is 2000 in month: ", index)
    else:
        print("In any month expense is not equals to 2000")
#  June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expense.append(1980)
print(expense)
# You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
expense[3] = expense[3] - 200
print(expense)

#   Exercise 2
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

print("Length of the list: ", len(heros))
# Add 'black panther' at the end of this list
heros.append("black panther")
print(heros)
#   You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heros.pop()
heros.insert(3, "black panther")
print(heros)
#   Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3] = ["doctor strange"]
print(heros)

# Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)

# Exercise 3
# Create a list of all odd numbers between 1 and a max number.
# Max number is something you need to take from a user using input() function

max_number = int(input(" Enter maximum number: "))
odd_number = []
for number in range(1, max_number + 1):
    if (number % 2) != 0:
        odd_number.append(number)
print(odd_number)
