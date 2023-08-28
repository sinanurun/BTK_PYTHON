treng = {"araba":"car","red":"Kırmızı","blue":"Mavi"}
print(treng)
print(type(treng))
print(treng.get("araba"))
print(treng["araba"])
print(treng.keys())
print(treng.values())
print(treng.items())
ikililer = treng.items()
print(type(ikililer))
for dd in treng:
    print(dd,treng.get(dd))
    print(treng[dd])