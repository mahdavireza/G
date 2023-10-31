import math

def f(I, k, a):
    result = -k + math.sqrt(k**2 + a**2 * I)
    return result

I = 2
k = 3
a = 4
f_result = f(I, k, a)
print(f_result)