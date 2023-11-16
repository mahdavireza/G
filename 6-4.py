def f(x, g_func):
    result = g_func(x) - (f(x) / (f(x) ** 2)) + (2 * x)
    return result