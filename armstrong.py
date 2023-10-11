digit=int(input("enter any number:"))
sum=0
order=len(str(digit))
a=digit
while(digit > 0):
    number=digit%10
    sum=sum+number**order
    digit=digit//10
    if sum==a :
        print("Armstrong number")
    else:
        print("not an armstrong number")

