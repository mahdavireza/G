def sort_list(inp_list):
    nums = []
    bools = []
    strings = []

    for elem in inp_list:
        if isinstance(elem, bool):
            bools.append(elem)
        elif isinstance(elem, int):  
            nums.append(elem)
        elif isinstance(elem, str): 
            strings.append(elem)
    
    nums.sort()  
    strings.sort() 

    return nums, bools, strings

# Example usage:
inp_list = [True, False, 'Hello', 3, 1, 'World', 2]
sorted_nums, sorted_bools, sorted_strings = sort_list(inp_list)
print(sorted_nums) 
print(sorted_bools)  
print(sorted_strings)  