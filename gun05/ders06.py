# 10.000"e kadar olan asal sayıların adetini ve geçen zamanı bulan program
from datetime import datetime
import math
sonDeger = 10000
sayac = 0
zaman = datetime.now()
# En küçük asal sayı olan 2 den istenilen değere kadar döngü kuruluyor
for deger in range(2, sonDeger): # Sırayla sayılar ele alınıyor
    kontrol = True  # Değerlerin kontrol edilmesi için ilk değer True veriliyor
# Asal olma özelliğinin kontrolü için bölenlerinin döngüsü kuruluyor
    for bolenSayi in range(2, int(math.sqrt(deger))+1):
        if deger % bolenSayi == 0:
            kontrol = False  # Tam bölme işlemi oluştuysa kontrol False yapılıyor
            break  # ve döngü sonlandırılıyor
    if kontrol:
        print(deger)
        sayac += 1  # Asal olma özelliği sağlanmışsa sayac arttırılıyor
print()  # Yeni satır başı
gecenZaman = datetime.now() - zaman  # İşlem tamamlandıktan sonra süre sonlandırılıyor
print("Adet:", sayac, " Geçen Zaman:", gecenZaman, " saniye")