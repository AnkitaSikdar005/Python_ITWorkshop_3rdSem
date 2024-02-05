def change_last_occurrence(input_string):
    if len(input_string) < 2:
        return input_string

    last_char = input_string[-1]
    modified_string = input_string[:-1].replace(last_char, '*') + last_char
    return modified_string

# Input a string from the user
input_str = input("Enter a string: ")

# Get the modified string and print the result
result_str = change_last_occurrence(input_str)
print("Modified string:", result_str)
