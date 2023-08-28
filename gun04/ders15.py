gorevler = []
while True:
    gorev = input("Yapıalcak bir görev giriniz (Bittiyse X giriniz)")
    if gorev.lower() == "x":
        break
    else:
        gorevler.append(gorev)
print(gorevler)
while gorevler!=[]:
    bitenler = []
    for dd in range(len(gorevler)):
        durum = input(f'{gorevler[dd]} görevinizi yaptınız mı ? e-h ?')
        if durum.lower() == "e":
            bitenler.append(dd)
    gorevler = gorevler - bitenler
else:
    print("Tüm görevler tamamlanmıştır")