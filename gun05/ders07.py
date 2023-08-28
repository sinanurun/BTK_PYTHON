dosya = open("deneme.txt", "r")
# for satir in dosya.readlines():
#     print(satir)
# print(dosya.readline())
# print(dosya.readline())
# print(dosya.readline())
metin = dosya.read()
satirlar = metin.split("\n")
print(satirlar)
for satir in satirlar:
    print(satir)