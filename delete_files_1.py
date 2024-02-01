import os

if os.path.exists("new.txt"):
    os.remove("new.txt")
else:
    print("this file does not exist")
    