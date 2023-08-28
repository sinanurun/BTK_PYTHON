#string işlemler - bölme ve parça alma işlemleri
ad = "Beyzakocyigit"
print(len(ad)) #len(x) x in boyutunu verir kaç elemandan oluştuğunu söyler
print(ad[5])# 5 indexli değeri verir
print(ad[-5]) # -5 indexli değeri verir
print(ad[::]) # başlangıç bitiş artış değeri
print(ad[:5]) # 0:5
print(ad[5:])
print(ad[5:8])
print(ad[::2])# 0:12:2
print(ad[3:10:3])

print(ad[::-1])
print(ad[-8:-5])
print(ad[-5:-8:-1])

print( "a" in ad)
print( "b" in ad)
print( "koc" in ad)