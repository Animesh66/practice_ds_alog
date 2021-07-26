sentence = input("Enter a String: ")
lowercase_sentence = sentence.lower()
char_string = lowercase_sentence.replace(" ", "")


def find_max_occurrence(char_string):
    if not char_string:
        print("You have not entered any string. Please enter a string to get the count")
        return 0, 0
    else:
        char_frequency = {}
        for char in char_string:
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1

        char_list = list(char_frequency.items())
        sorted_list = sorted(char_list, key=lambda key_value: key_value[1], reverse=True)
        count = 0
        list_length = len(sorted_list)
        final_list = []
        while count != list_length - 1:
            i, j = sorted_list[count]
            k, l = sorted_list[count + 1]
            if j == l:
                if (i, j) not in final_list:
                    final_list.append(sorted_list[count])
                    final_list.append(sorted_list[count + 1])
            count += 1
        if not final_list:
            final_list = sorted_list[0]
        set(final_list)
    return final_list

print(find_max_occurrence(char_string))

# character, occurrence = find_max_occurrence(char_string)
# if character != 0:
#     print(f" '{character}' is repeated highest and its occurrence is {occurrence} times ")
