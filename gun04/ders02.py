ogrenci_ad = input("Adınızı giriniz")
ogrenci_soyadi = input("Soyadınızı giriniz")
ogrenci_yas = int(input("Yaşınızı giriniz"))
ogrenci_boy = float(input("Boyunuzu giriniz"))
ogrenci_cinsiyet = bool(int(input("cinsiyetinizi giriniz E:1, K:0")))

ogrenci = [ogrenci_ad, ogrenci_soyadi, ogrenci_boy, ogrenci_yas, ogrenci_cinsiyet]
print(ogrenci)
print(ogrenci[0])
print(type(ogrenci))
print(type(ogrenci[-1]))
print(len(ogrenci))

for eleman in ogrenci:
    print(eleman)