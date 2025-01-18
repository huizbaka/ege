from functools import *

a = list(map(int, str(2 ** 63 - 1)))
@cache
def f(s, l, fl):
    if l == 0: return s == 159
    return sum(f(s + x, l - 1, fl and (x == a[-l])) for x in range([10, a[-l] + 1][fl]))
print(f(0, len(a), 1))