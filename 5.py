def clear_list(input_list):
    for item in input_list:
        input_list.remove(item)
    return input_list

my_list = [1, 2, 3, 4, 5] 
cleared_list = clear_list(my_list)
print(cleared_list) # []