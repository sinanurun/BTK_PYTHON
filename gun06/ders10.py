# **kwargs ise keywordli argumanlar almamızı sağlar
# kwargs ise dict tipinde veri oluşturur
def o_karti(**kwargs):
    print(kwargs)
    o_bilgiler = {**kwargs}
    print(o_bilgiler)
o_karti(o_adi="Esra",o_no=35,o_sehir="İzmir")