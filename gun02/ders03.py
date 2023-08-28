yol = int(input("Otoban uzunuğunu giriniz : "))
zaman = float(input("Yolculuk süresini giriniz"))
hiz = yol / zaman
if hiz > 132:
    print("Hız cezası aldınız")
else:
    print("hız kurallarına uydg için teşekkürler")