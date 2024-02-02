try:
    f=open("hehe.txt",w)
    try:
        f.write("hello")
    except:
        print("file is not found")
except:
    print("file have some error")          
        