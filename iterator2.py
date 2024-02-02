class Num:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        x=self.a
        self.a +=1
        return x
 
    
n1=Num()
iterator_wala = iter(n1)

print(next(iterator_wala))
print(next(iterator_wala))
print(next(iterator_wala))
print(next(iterator_wala))
print(next(iterator_wala))