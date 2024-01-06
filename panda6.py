import pandas as pd

mydata={
    "cars" : ['BMW','AUDI','TOYOTA'],
    "quantity":[12,34,55]
}

var=pd.DataFrame(mydata)
#it was usually use for multi dimension table

print(var)
print("......................................................")
print(var.loc[0])
print(var.loc[[0,1]]) 
#to check the location of exact index