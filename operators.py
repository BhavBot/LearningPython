#arithmetic operators
v=10/3
print(v)
v2=10//3
print(v2)
v3=3//2
print(v3)

r=7%2
print(r)
r2=100%10
print(r2)

n=3500000000000000000000353535353535353535
if (not n%5 and not n%7):
    print("true")
else:
    print("false")
exponent=2**10
print(exponent)
#assignment operators
a=7
a+=1
#same as a=a+1
print(a)
a-=1
print(a)
a*=3
print(a)
a%=3
print(a)
a**=100000000000000
print(a)
#comparision operators
print(7==3)
print(4==8/2)
print(7!=3)
print(7>3)
print(7<3)
print(3>=5)
print(3<=5)
#logical operators
a=6
b=89
if (a<=6 and b>10):
    print("coreect")
else:
    print("not coreect")

if (a<6 or b>100):
    print("coreect")
else:
    print("not coreect")

if not(a<=6 and b>10):
    print("coreect")
else:
    print("not coreect")
#bit wise operators
print(0b1001)
x=0b101
y=0b111
print(x & y)
print(x | y)
print(~x )
print(x ^ y)
print(bin(10))
print(x>>2)
print(x<<2)
print(bin(x<<2))
#identity operators
x1=5
y1=5
x2="hello"
y2="hello"
x3=[1,2,3]
y3=[1,2,3]
print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)
#membership operators
#this you can use it on strings,tuples,lists,dictionaries and sets
msg="hello world"
dict1={"bhavesh":18,"anil":46}
array1=[234,124,123,5,2]
set1={10,20,30,30,40}
print("o worl" in msg) #worl be like
print("bhavesh" not in dict1)
if 100 in array1:
    print("coreect")
else:
    print("not coreect")
#()
x=10-4*2
print(x)
y=(10-4)*2
print(y)
#[]
print(array1[3])
str2="my name is bhavesh()()()"
slice1=str2[4:12]
print(slice1)
range1=range(100,200)
for r in range1:
    print(r)
array2=list(range1)
print(array2)
array3=array2[50:70]
print(array3)
array4=array2[50:70:3]
print(array4)                                        #if is is if then:
print(array4)                                            #print("haha")
print(array2[::-1])
print(array2[50:])
print(array2[:30])