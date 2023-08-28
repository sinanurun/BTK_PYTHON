tek_adet = 0
cift_adet = 0
tek_toplam = 0
cift_toplam = 0
for dd in range(1,5):
    print(f'{dd} . sayıyı giriniz')
    sayi = int(input())
    if sayi % 2 == 1:
        tek_adet += 1
        tek_toplam += sayi
    else:
        cift_toplam += sayi
        cift_adet += 1
print(f'girdiğiniz tek sayıların ortalaması {tek_toplam/tek_adet}')
print(f'girdiğiniz tek sayıların ortalaması {cift_toplam/cift_adet}')