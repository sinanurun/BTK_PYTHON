def birinci():
    print("program başlatma fonksiyonu")
    ikinci()

def ikinci():
    print("sonradan çalışan fonksiyon")

if __name__ == '__main__':
    birinci()
