listleb=[2,4,3,21,1]
listlem=[123,3,34,43123,3456,12234,1]
for x,y in zip(listleb,listlem):
    print(x,y)

listsort=sorted(listleb)
print(listsort)

maxger=max(listleb)
print(max)

kamz=max(listlem)

mapp=map(lambda k: k**2,listlem)
print(list(mapp))

phi=filter(lambda k: k%2==0,listleb)
print(list(phi))

#i have already learnt sum, 
# sorted, 
# max, 
# min, 
# and enumerate. 
# and then one more i think oh no yeah thats it yeah thats it