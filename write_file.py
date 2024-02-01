f=open("file.txt","w")
f.write("oops file is deleted")
f.close()

#we need to re open the file and use read not readline
f=open("file.txt","r")
print(f.read())