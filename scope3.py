x=100  #it used as globally and used by all

def myfunc():
    x=200         #local variable always have first priority
    print(x)
 
myfunc()

print(x)    