class Person:
    def __init__(self,name,age,phone):
        self.name=name
        self.age=age
        self.phone=phone
        
    def myfunc(self):
        print(".....................................................")
        print("Hello this is my bio: "+self.name,self.age,self.phone)
        print(".....................................................")
     
p1=Person("Priya",22,7978787877)
p1.myfunc()

p2=Person("Duggu",21,890098890) 
p2.myfunc()



           