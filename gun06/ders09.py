# *args bize n tane parametre geleceğini belirtir args ise tuple tipinde veri oluşturur
def sayiyazdir(*sayilar):
    x = [*sayilar]
    print(x)
    print(*sayilar)
    print(sayilar)
    print(type(sayilar))
    for sayi in x:
        print(sayi)
sayiyazdir(1,2,3,4,5,6)

