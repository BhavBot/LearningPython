t1=()
t2=(1,3,5)
t3=1,
t4=tuple((123,2,334,23,135))
print("Empty tuple: ",t1)
print("Regular tuple: ",t2)
print("Comma seperated tuple: ",t3)
print("Tuples constructor: ",t4)
print("Lentgh: ",len(t4))
print(t2[2])
for k in t2:
    print(k)
if 334 in t4:
    print("confemr")
#t4[3]=1231231322123123123123123123123123123123123123123123123123123123123123123123123123123
#del(t2)
#print(t2)
yo={"yo":"oy",200:"L","green":"chlorophyll"}
for key,value in yo.items():
    print(f"key is {key}")
    print(f"value is {value}")
a,b,c=t2
print(f"Unpacking of tuple: {a} {b} {c}")
print(t4.index(334))
print(t4.count(334))
    
    
