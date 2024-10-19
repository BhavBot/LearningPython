n=input("n")
r=range(int(n))
print(r)
l=list(r)
l.pop(0)
l.append(int(n))
print(l)
f=1
for y in l:
    f=(y*f)
print("factorial=",f)
#the cruel(not crude) method
i=int(n)
f=1
while i>=1:
    f*=i
    i+=-1
print("weird method:",f)



