# default parametreli fonksiyonlar
# öncelikle gerekli olanlar, sonra default tanımlı olan parametreler yazılmadılır
# def daire(r, pi):
#     alan = pi * (r**2)
#     return alan
# print(daire(3,5))

# def daire(r,pi=3.14):
#     alan = pi * (r**2)
#     return alan
# print(daire(5,3))

def daire(r, pi=3.14):
    alan = pi * (r ** 2)
    return alan

print(daire(5))
