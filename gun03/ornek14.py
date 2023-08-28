tutulan = 87
taban = 0
tavan = 100
tahmin = int(input("Bir sayı giriniz"))
while True:
    if taban < tahmin < tavan:
        break
    else:
        tahmin = int(input("Uygun Bir sayı giriniz"))

while not(tutulan == tahmin):
    if tahmin> tutulan:
        tavan = tahmin
        tahmin = int(input("daha küçük Bir sayı giriniz"))
        while True:
            if taban < tahmin < tavan:
                break
            else:
                tahmin = int(input("Uygun Bir sayı giriniz"))
    else:
        taban = tahmin
        tahmin = int(input("daha büyük Bir sayı giriniz"))
        while True:
            if taban < tahmin < tavan:
                break
            else:
                tahmin = int(input("Uygun Bir sayı giriniz"))
else:
    print("tebrikler bildiniz")

while True:
    if tahmin == tutulan:
        print("tebrikler bildiniz")
        break
    elif tahmin> tutulan:
        tahmin = int(input("daha küçük Bir sayı giriniz"))
    else:
        tahmin = int(input("daha büyük Bir sayı giriniz"))