def F(n):

    if n == 0:
        return 0

    if n <= 2:
        return n
    else:
        return F(n-1)*F(n-2)


result = F(6)
print(result)
