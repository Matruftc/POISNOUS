fruits=("mango","cherry","banana","litchi")

(red,yellow,green,white)=fruits
print(red)
print(yellow)
print(green)
print(white)

print(".......................................")

fruits=("mango","cherry","banana","litchi")

(red,*yellow)=fruits
print(red)
print(yellow)


print(".......................................")

fruits=("mango","cherry","banana","litchi")

(red,*yellow,white)=fruits
print(red)
print(yellow)
print(white)
