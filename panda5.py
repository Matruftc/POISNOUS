import pandas as pd

mydata={
    "cars" : ['BMW','AUDI','TOYOTA'],
    "quantity":[12,34,55]
}

var=pd.DataFrame(mydata)
#it was usually use for multi dimension table

print(var)
