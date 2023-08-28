bas = int(input("başlangıç değerini giriniz"))
bitis = int(input("bitiş değerini giriniz"))
artis = int(input("artis değerini giriniz"))
toplam = 0
while bas < bitis:
    print(bas)
    toplam += bas
    bas += artis
else:
    print("hesaplama tamamlanmıştır")
print("girilen sayıların toplamı ", toplam)