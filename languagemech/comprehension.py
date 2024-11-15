#comprehension
ar=[1,4,6,7,11]
squares=[n*n for n in ar ]
print("basic list comp",squares)
dictosquares={n:n*n for n in ar}
print("dict comp",dictosquares)
#n*n/n=1/n???
setofloats={n/(n*n) for n in ar}
print("set comp",setofloats)
names=["name1","bhavesh","me","myself","I"]
idnames=[(n,name) for n in ar for name in names]
print("tuple comprehension",idnames)
#matrix time
matrix=[[n*i for i in range(2,7)] for n in ar]
print("nested comp",matrix)
bruh3Dmatrix=[[[n*i*j for j in range(3,9)] for i in range(2,7)] for n in ar ]
print("2 levels nested comp",bruh3Dmatrix)
#ternery if condition haajhga
evenodd="even" if 4%2==0 else "wrong"
print("ternary if statement",evenodd)
numbersgreaterthanx=[n if n>6 else "stop" for n in ar]
print("ternery if statement in list comp",numbersgreaterthanx)
numbersgreater2thanx=[n for n in ar if n>6]
print("regular if statement in list comp",numbersgreater2thanx)
