pazar = ["elma","armut","incir","karpuz","üzüm","kavun"]

print(pazar)
print(pazar[3])
print(pazar[:2])
print(pazar[-2::])
print(pazar[3:5])

pazar.append("çilek")
print(pazar)
pazar.append("armut")
print(pazar)
print(pazar.count("armut"))
print(len(pazar))
print(pazar.index("armut"))
pazar.insert(1,"ayva")
pazar.insert(1,"kivi")
print(pazar)
pazar.pop(0)# parametre verilemz ise son elemanı siler
pazar.remove("kavun")
print(pazar)
pazar.sort()
print(pazar)
pazar.reverse()
print(pazar)

dayipazar = ["domates", "biber"]
pazar.extend(dayipazar) # pazar = pazar + dayipazar
print(pazar)
pazar.clear()
print(pazar)
del pazar
print(pazar)