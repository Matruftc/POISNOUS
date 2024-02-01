f=open("file.txt","a")
f.write("hey i am your big bro")
f.close()

#we need to re open the file and use read not readline
f=open("file.txt","r")
print(f.read())