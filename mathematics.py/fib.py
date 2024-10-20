fib=[1,1]
i=input("n: ")
n=0
m=1
if int(i)<=1:
    print("fibbanachi sequence till 1 term:",[fib[0]])
else:
    while (len(fib))!=int(i):
        fib.append(fib[n]+fib[m])
        n+=1
        m+=1
if int(i)>1:
    print(f"fibbanachi sequence till {i} terms:",fib)
                                            #print(len(fib))
                                            #print(fib)
                                            #print(n)
                                            #print(m)
   #THis is a coool prograam 0_0                                         
