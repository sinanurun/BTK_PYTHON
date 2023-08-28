#bilgi giriş işlemleri input() ile olur
print("adınız nedir")
isim = input()
print("memnun oldum", isim)
print(type(isim))
print(isim,"yaşın kaç")
yas = int(input())
print(isim,"sen",yas,"yaşındasın")
print(type(yas))
#print(isim,"boyun kaç ?")
boy = float(input("Boy Bilgisi Giriniz : "))
"""
soru = isim+"boyun kaç ?"
boy = float(input(soru))
"""
print(isim,"senin boyun",boy)
print(type(boy))
