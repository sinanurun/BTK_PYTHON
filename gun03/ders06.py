baslangic = int(input("Başlangıç değeri giriniz"))
bitis = int(input("Baitiş değeri giriniz"))
artis = int(input("Artiş değeri giriniz"))
faktoriyel = 1
for dd in range(baslangic,bitis,artis):
    faktoriyel *= dd
    print(dd, faktoriyel)
