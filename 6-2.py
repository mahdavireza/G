def find_char_index(string, char):
    if char in string:
        index = string.index(char)
        print('The index of character "{}" in the string is: {}'.format(char, index))
    else:
        print('The character "{ok}" is not in the string.'.format(char))

# Test the function
find_char_index('Hello, World!', 'W')