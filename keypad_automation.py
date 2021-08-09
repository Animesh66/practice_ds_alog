user_input = input("Enter a string: ")
mobile_key = {'ABC': 2, 'DEF': 3, 'GHI': 4, 'JKL': 5, 'MNO': 6, 'PQRS': 7, 'TUV': 8, 'WXYZ': 9}
user_output = []


def test_function(letters):
    for letter in letters:
        for l, v in mobile_key.items():
            if letter in mobile_key[l]:
                return user_output.append(v)


print(test_function(user_input))
