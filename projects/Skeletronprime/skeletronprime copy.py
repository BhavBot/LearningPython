r=range(2,20)
l=list(r)
n=2
m=1
while m!=0:
    while l[n]%l[m]!=0:
        if n>19:
            break 
        elif m!=1:
            m-=1
            continue
        elif m==1:
            n+=1
            m=(n-1)
            continue
        elif l[n]%l[m]==0:
            l.pop(n)
            n+=1
            m=(n-1)
            print(m)
            print(n)
            continue
        if n>19:
            break 
print(l)
print(m)
    
    
    
