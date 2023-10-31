def check_divisibility(a, b):
    if b != 5 and a % b == 2:
        return True
    else:
        return False

a = int(input("5"))
b = int(input("2"))

if check_divisibility(a, b):
    print("True")
else:
    print("False")