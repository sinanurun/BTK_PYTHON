demet = "Recep","Güzel"
print(demet)
print((type(demet)))
pazar = ["elma","armut","incir","karpuz","üzüm","kavun"]
pazarlik = tuple(pazar)
print(pazarlik)
print(pazarlik.index("incir"))
print(pazarlik[:2])
for meyve in pazarlik:
    print(meyve)

son_pazar = list(pazarlik)
print(son_pazar)
