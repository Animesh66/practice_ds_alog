def return_string_frequency():
    try:
        word = input("Enter a string: ")
        new_string = word.lower()
        converted_string = new_string.replace(" ", "")
        char_frequency = {}
        for char in converted_string:
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1
        sorted_char_frequency = sorted(char_frequency.items(), key=lambda kv: kv[1])
        return sorted_char_frequency[-1]
    except IndexError:
        print("Invalid string")


if __name__ == "__main__":
    maximum_freq = return_string_frequency()
    print(maximum_freq)
