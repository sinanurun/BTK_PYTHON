x = 50
def myfunc():
    global  x
    x = 300
    print(x)
def fonk2 ():
	print(x)

fonk2()
myfunc()
fonk2()