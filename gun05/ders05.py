import datetime
import time
time.sleep(5)
a = input("ilk bilgiyi giriniz")
giris = datetime.datetime.now()
b = input("ikinci bilgiyi giriniz")
cikis = datetime.datetime.now()
fark = cikis - giris
print(fark.microseconds)
