ad1 = "Recep"
ad2 = "ilayda"
ad3 = "esra"
metin = "Merhaba {} eğitime hoşgeldiniz "
print(metin.format(ad1))
print(metin.format(ad2))
print(metin.format(ad3))
print(metin)
metin2= "Merhaba {}, {}, {} eğitime hoşgeldiniz "
print(metin2.format(ad1,ad2,ad3))
metin3 = "Merhaba {k1}, {k2}, {k3} eğitime hoşgeldiniz ".format(k1 = ad2, k2= ad1, k3= ad3)
print(metin3)