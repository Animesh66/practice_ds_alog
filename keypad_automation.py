user_input = input("Enter a string: ")
mobile_key = {'ABC': 2, 'DEF': 3, 'GHI': 4, 'JKL': 5, 'MNO': 6, 'PQRS': 7, 'TUV': 8, 'WXYZ': 9}
user_output = []


def test_function(letters):
    new_letters = letters.upper()
    for letter in new_letters:
        for l, v in mobile_key.items():
            if letter in l:
                user_output.append(v)
                break
    return user_output


print(test_function(user_input))
