kizlar = ["emine","esra","ilayda"]
erkekler = ["ali","recep","emre"]
liste = [kizlar,erkekler]
for dd in range(len(liste)):
    for kisi in range(len(liste[dd])):
        print(liste[dd][kisi], end= "  ")
        print(dd,kisi)