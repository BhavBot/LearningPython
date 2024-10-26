def method(number,name,n):
    print("regular methods are positional parameters with no default values.")
    print(number,name,n)
method(9,"me","n")
def methdefault(number,name="anil"):
    print("default parameters: ","numebr: ",number,"name: ",name)    
methdefault(123,"me")
def methwithmultireturn(number=1, name="somename",):
    print(number,name)
    return number,name
x,y=methwithmultireturn()
print("method returning with multiple returns",x,y)
def metharbitary(*args):
    i=1
    for arg in args:
        print(i,arg)
        i+=1
metharbitary("ok",25,"hahahahahahahahaha","lump","geometry dash","bwomp")
def kewwordargs(**kwargs):
    for k,value in kwargs.items():
        print("k:",k,"value:",value)
kewwordargs(ha="ah",nooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo="yes")
def starinthestart(*,ok,name="mnbgfe",number,system,obliqe,transparent,mouse,rat,food,fan,cornflakes,cereal,ceiling,gum,okfine):
    print(ok,name,number,system,obliqe,transparent,mouse,rat,food,fan,cornflakes,cereal,ceiling,gum,okfine)
starinthestart(ok=123,number=546,system=5,obliqe=23,transparent=4,mouse=235,rat=7,food=234,fan=5,cornflakes=623,cereal=456,ceiling=23,gum=12344123,okfine=1345)
mylambda1=lambda: print("first ever lambda")
mylambda1()
mylambda2=lambda arg1: print("lambda with args: ",arg1)
mylambda2(190130984109819821928418095)
liston=[123,234,345,45,6456,234]
neewlsit=list(filter(lambda X:X%3==00,liston)) #i types every number divisible by 3 randomly
print("using lambdas to filter: ",neewlsit)
#equvilant of lambda
def iseven(X):
    return X%3==0
newlistoff=list(filter(iseven,liston))
print("using regular methods to filter: ",newlistoff)
names=[{"name":"bhaevsh","height":100000,"age":"unknown"},
         {"name":"akchiol","height":3,"age":2.5},
         {"name":"rothivk","height":9,"age":200}]
sortedbyname=sorted(names,key=lambda d:d["name"])
print("sorted by names using lambdas: ",sortedbyname)
sortedbyheight=sorted(names,key=lambda d:d["height"],reverse=True)
print("sorted by height: ",sortedbyheight)
def directmeth():
    print("tsup")
    def innermeth():
        print("innermeth")
    innermeth()
directmeth()
def recursionmeth(n):
    print("intial n:",n)
    if n==1:
        return 1
    else:
        return (n*recursionmeth(n-1))
factorial=recursionmeth(5)
print("factorial from recursion",factorial)
#is a factorial a multidimensional spiral







