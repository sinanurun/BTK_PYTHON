# part 1
""""
adet = int(input("Kaç edet zerzevat alacaksınız"))
zerzevat = []
for dd in range(1, adet + 1):
    urun = input(f'{dd}, nolu ürünüzü giriniz')
    zerzevat.append(urun)
print("pazar listeniz", zerzevat)
"""

# part 2
mesaj = """"
pazar listesi programına hoşgeldiniz,
programdan çıkmak için x'e basınız
"""
print(mesaj)
zerzevat = []
while True:
    urun = input("Ürün girişi yapın veya  X'e basınız")
    if urun.lower() != "x":
        zerzevat.append(urun)
    else:
        print("pazar Listesiniz", zerzevat)
        break
