#sort.py
names=[{"name":"bhaevsh","height":100000,"age":20000000},
         {"name":"achiol","height":3,"age":2.5},
         {"name":"ruuthivk","height":9,"age":200}]
snames=sorted(names,key= lambda d:d["age"])
print(snames)
lsnames=sorted(names,key=lambda d:len(d["name"]))
print(lsnames)
integers=[1,5,-1,345,-123,-12,45,-512,456]
abssintegers=sorted(integers,key=lambda i:abs(i),reverse=True)
print(abssintegers)
print(abssintegers[0])
print(max(names,key=lambda d:d["height"]))
print(min(names,key=lambda d:d["age"]))
