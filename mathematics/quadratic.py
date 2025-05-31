import math


a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
d=((b**2)-(4*a*c))
if d>0:
    alpha=(-b+math.sqrt(d))/2*a
    beta=(-b-math.sqrt(d))/2*a
    print(alpha, beta)
elif d<0:
    d=d-2*d
    alpha=(-b+math.sqrt(d))/2*a
    beta=(-b-math.sqrt(d))/2*a
    print(alpha,"i ", beta,"i ",sep="")

