#  i t e r a t o r
# __iter__() 
# __next__()
# fib2.0

class Fib:
    i=0
    lafib=1
    seclafib=1
    max=10
    def __init__(self,max):
        self.max=max
    def __next__(self):
        if self.i>self.max:
            raise StopIteration
        if self.i==0 or self.i==1:
            self.i+=1
            return 1    
        else:
            toberet=self.lafib+self.seclafib
            self.seclafib=self.lafib
            self.lafib=toberet
            self.i+=1
            return toberet
    def __iter__(self):
        return self
    
if __name__=="__main__":
    ok=Fib(100)
    dict1={}
    # print(type(Fib(12)))
    # ok2=list(Fib(100))
    print(next(ok))
    print(next(ok))
    print(next(ok))
    print(next(ok))
    print(next(ok))
    
    for i,f in enumerate(ok):
        print(str(i)+":"+str(f))
        dict1[i]=f
        
    # print(enumerate(ok))
    # print(dict1[100])
    # print(dict1[23])
    
    
                
        
    


