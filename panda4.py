import pandas as pandu

mynum=[2013,2014,2015]

var=pandu.Series(mynum, index=['x','y','z'])
#with an index argument

print(var)
print(var['y']) #it shows only index y value