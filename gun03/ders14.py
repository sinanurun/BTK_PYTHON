adet = int(input("kaç tane sayıyı hesaplamak istiyorsun"))
carpim = 1
while True:
    sayi = int(input("Bir sayı giriniz"))
    if sayi == 0 or adet == 0:
        print("giridğiniz sayıların çarpımı", carpim)
        break
    adet -= 1
    if sayi == 111:
        continue
    carpim *= sayi
