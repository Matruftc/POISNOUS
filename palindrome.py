num=151
actual=0
a=num
while (num > 0):
    test=num%10
    rev=test
    actual=actual*10+rev
    num=num//10
    print(actual)
if(a==actual):
    print("Palindrome")
else:
    print("not a palindrome num")