sayilar = []
for dd in range(10):
    sayilar.append(int(input(f'{dd + 1}. sayıyı giriniz')))
eb = sayilar[0]
ek = sayilar[0]
for sayi in sayilar:
    if eb < sayi:
        eb = sayi
    if ek > sayi:
        ek = sayi
print("en büyük", eb)
print("en büçük", ek)
