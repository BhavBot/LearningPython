
T=True
F=False
N=None
list=None
if F:
    list=[1,2,3]
if list!=None:
    print(list)

my_dict={"happy":"sad","angry":"sad"}

set1={"A","E","I","O","U"}

print(set1)

tuple1=("1","2","3")

array1=["egg","eg","meat"]

list1=("ten",3.14,13,array1,tuple1,set1,None)

print(list1)

for k in list1:
    print(type(k))

set2={"hello",tuple1,1,1,"whats up","whats up"}
print(set2)

for i in set2:
    print(type(i))

tuple2=("ten",120,6.28,array1,tuple1,set2)
print(tuple2)
for o in tuple2:
    print(type(o))