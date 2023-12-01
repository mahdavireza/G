def insert_chars(input_str, big_char, small_char):
    output_str = ""
    for i, char in enumerate(input_str):
        output_str += char
        if i%2 == 0:
            output_str += big_char
        else:
            output_str += small_char
    
    return output_str
str = "hello"
big_char = "X" 
small_char = "x"

print(insert_chars(str, big_char, small_char))