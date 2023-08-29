def azaltan(n):
    if n != 0:
        print(n)
        return azaltan(n-1)
    else:
        return 0
print(azaltan(1000))