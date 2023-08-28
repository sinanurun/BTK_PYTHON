ders_sayisi = int(input("Toplam Kaç Dersiniz Var ? "))
genel_ortalama_toplami = 0
for ders in range(1, ders_sayisi + 1):
    print(ders,", derste kaç sinavınız var")
    sinav_sayisi = int(input())
    toplam = 0
    for sinav in range(1, sinav_sayisi+1):
        print(ders, "dersinin,", sinav, "sınav notu")
        sinav_puani = int(input())
        toplam += sinav_puani
    ortalama = toplam/sinav_sayisi
    genel_ortalama_toplami += ortalama
sonuc_ortalamasi = genel_ortalama_toplami/ders_sayisi
print("derslerinizin genel ortalaması ", sonuc_ortalamasi)
        