def faktoriyel(n):
    if n != 0:
        return n * faktoriyel(n-1)
    else:
        return 1
print(faktoriyel(5))