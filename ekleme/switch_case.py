'''
python 3.12 ile gelen Switch case örneği 
'''

yas = 18 

match yas:
    case 18:
        print('Siz erişkin bir bireysiniz')
    case 16:
        print('motor ehliyeti alabilecek yaştasınız')
    case _: 
        print('diğer durum içi yaş bilgisi yok')