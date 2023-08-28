# iç içe listeler, çok boyutlu listeler
sebze = ['domates', 'biber']
meyve = ['üzüm', 'çilek', 'kivi', 'karpuz', 'incir', 'ayva', 'armut', 'armut']
sark = ["peynir", "helva", "bal"]
yesillik = ["roka", "maydanoz", "tere"]
pazar_listesi = [sebze, meyve, sark, yesillik, "baklava"]
print(pazar_listesi)
print(pazar_listesi[0][0])
print(pazar_listesi[1][1])
for dd in pazar_listesi:
    if type(dd) is list:
        for urun in dd:
            print(urun, end="\t")
        print()
    else:
        print(dd)
