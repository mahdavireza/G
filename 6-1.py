def reverse_string(str):
    reversed_str = ''
    length = len(str)
    while length > 0:
        reversed_str += str[length - 1]
        length -= 1
    return reversed_str
print(reverse_string("Hello World"))  # Output: dlroW olleH