#Dictionary
#keys are immutable. keys can be tuples,strings or integers
dict1={1:10,3:20,2:15}
print(dict1[2])
dict1[40]=3.14
print(dict1[40])
#dict1.clear()
print(dict1)
dict1.pop(2)
print(dict1)
del dict1[1]
print(dict1)
dict2=dict1.copy()
dict3=dict1
print("dict1: ",dict1)
print("dict2: ",dict2)
print("dict3: ",dict3)
dict1[98]=890
print("dict1: ",dict1)
print("dict2: ",dict2)
print("dict3: ",dict3)
dict3[87]=["me",2000]
print("dict1: ",dict1)
print("dict2: ",dict2)
print("dict3: ",dict3)
dict4=dict3.copy()
print("dict4: ",dict4)
array4=dict3[87]
print(array4)
array4[0]="you"
print(array4)
print("dict1: ",dict1)
print("dict2: ",dict2)
print("dict3: ",dict3)
print("dict4: ",dict4)
print("printing keys",dict1.keys())
print("printing values",dict1.values())
print("printing items",dict1.items())
dict1.setdefault(56,900)
print("testing setdefault",dict1[56])
dict1[56]=54
print("testing setdefault",dict1[56])
popped=dict1.pop(56)
print("testing pop",popped)
print("testing get",dict1.get(56))
print("testing get",dict1.get(56,4567))
print(dict1)
poppeditem=dict1.popitem()
print("testing popitem",poppeditem)
print(dict1)
dict1[3]=[123,234,345,456,567,789,890]
dict5={9:90,8:80}
print("testing update",dict1)
print("testing update",dict5)
dict5.update(dict1)
print("testing update",dict1)
print("testing update",dict5)
dict5[8]=8000
print("testing reference",dict1)
print("testing reference",dict5)
dict1[3][0]=321123321123321123321123321123321123
print("\033[30mtesting reference\033[34m",dict1)
print("\033[30mtesting reference\033[34m",dict5)
print("\033[32mThis text will be green\033[31m BLACK\033[0m",)
dict6=dict.fromkeys(dict1,"defaultvalue")
print("testing fromkeys",dict6)
dict7={"name":"dictseption","internaldict":dict6}
print("testing nested dicts",dict7)
print("accesing sub dict",dict7["internaldict"][3])

