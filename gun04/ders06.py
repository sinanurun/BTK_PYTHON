# iç içe listeler, çok boyutlu listeler
sebze = ['domates', 'biber']
meyve = ['üzüm', 'çilek', 'kivi', 'karpuz', 'incir', 'ayva', 'armut', 'armut']
sark = ["peynir", "helva", "bal"]
yesillik = ["roka", "maydanoz", "tere"]
# pazar_listesi = [sebze, meyve, sark, yesillik]
# for dd in pazar_listesi:
#     index = pazar_listesi.index(dd)
#     for urun in dd:
#         index2 = dd.index(urun)
#         print(pazar_listesi[index][index2])
pazar_listesi = [sebze, meyve, sark, yesillik]
for dd in range(len(pazar_listesi)):
    for urun in range(len(pazar_listesi[dd])):
        print(pazar_listesi[dd][urun])