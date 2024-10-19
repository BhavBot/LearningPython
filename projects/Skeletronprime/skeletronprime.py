j=input("n: ")
r=range(2,200)
u=range(1,200)
v=list(u)
l=list(r)
m=1
n=0

print(l)
for i in l:
    if l[m]%l[n]==0:
        l.pop(m)
        
        continue
    else:
        n-=1
        continue
print(l)
    