a = 67
def ds(x):
    if x//3 >= 5:
        return ds(x//3), ds(x-1)
    elif x-1 >= 5:
        return ds(x-1)
    else:
        return x

print(ds(a))
print(str(ds(a)).count(')), ('))