def myfunc():
    global x   # using global keyword for accessing the global variable
    x=320
    print(x)
 
myfunc()

print(x)    