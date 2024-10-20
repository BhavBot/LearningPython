import math
n=input("n: ")
i=0
sum_=0
while i<int(n):
    sum_+=(i+i)+1
    print(sum_)
    i+=1
print("n^2:",sum_)
print(f"sqrt of {sum_}:",math.sqrt(sum_))

    
    