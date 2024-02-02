def myfunc():
    x=100
    def innerfunc():
        print(x)
        innerfunc()  
myfunc()              