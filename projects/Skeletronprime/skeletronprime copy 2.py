r=range(3,20,2)
l=list(r)
x=2
for i in l:
    if i%(i-x)==0:
        l.pop(i)
        continue
    elif i%(i-2)!=0:
        x-=2
        continue
        
l.insert(0,2)
    
print(l)
