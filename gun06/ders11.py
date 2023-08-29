def o_karti(*args,**kwargs):
    print(args)
    print(kwargs)
    o_bilgiler = {**kwargs}
    print(o_bilgiler)
o_karti("YBS","Bilecik",o_adi="Esra",o_no=35,o_sehir="İzmir")