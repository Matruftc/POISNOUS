fruits=("apple","banana","chery","coconut","litchi","guava")
print(fruits)

x=list(fruits)
x[0]="avocado"        #adding in initial part or add through index part
x.append("basil")     #adding ar last part
x.remove("banana")    #use for remove some items
fruits=tuple(x)
print(fruits)
print(type(fruits))


