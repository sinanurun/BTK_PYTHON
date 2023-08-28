sayi1 ,sayi2, sayi3 = int(input("bir sayı giriniz")), int(input("bir daha sayı giriniz")), int(input("bir tane daha sayı giriniz"))
if sayi1>=sayi2>=sayi3: # sayi1>sayi2 and sayi2 > sayi3
    print(sayi1, sayi2, sayi3)
elif sayi1>sayi3>sayi2:
    print(sayi1, sayi3, sayi2)
elif sayi2>sayi3>sayi1:
    print(sayi2, sayi3, sayi1)
elif sayi2>sayi1>sayi3:
    print(sayi2, sayi1, sayi3)
elif sayi3>sayi1>sayi2:
    print(sayi3, sayi1, sayi2)
else:
    print(sayi3, sayi2, sayi1)