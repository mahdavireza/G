a = [1, 5, 6]
b = [7, 8, 9]  
c = [1, 7, 5, 8, 6, 9]

for item in set(a).intersection(set(b)).intersection(set(c)):
    print(item)