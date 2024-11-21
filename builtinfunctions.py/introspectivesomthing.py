# id, type, instanceof, dir, local, global,help, callable, hasattr, repr, are all the things in this thing
dictwithlist={"yoooo":["yo1","yo2"],"woah":[234,23456]}
id1=id(dictwithlist["yoooo"]) #yahoo
print(id1)
myyu=dictwithlist["yoooo"]
myyuid=id(myyu) 
print(myyuid)

print(type(dictwithlist["yoooo"]))

print(type(dictwithlist["woah"]))

if type(dictwithlist["yoooo"])==type(dictwithlist["woah"]):
    print("coreect it is coreect")
else:
    print("wrong try again")

class Fullstyle:
    pass
class Rajinistyle(Fullstyle):
    pass

full=Fullstyle()
rajini=Rajinistyle()
if isinstance(full,Fullstyle):
    print("print(it is full style)")
else:
    print("aint full")
    
if isinstance(full,Rajinistyle):
    print("print(full is rajinistyle)")
else:
    print("full aint rajini style")
    
if isinstance(rajini,Fullstyle):
    print("print(rajini is Fullstyle)")
else:
    print("rajini aint fullstyle")
    
if isinstance(rajini,Rajinistyle):
    print("print(rajini is rajinistyle)")
else:
    print("rajini aint rajinistyle")
    
straing="straing"
srting="straing"

if isinstance(straing,str):
    print("is string")
else:
    print("print aint string ")
    
if isinstance(dictwithlist["yoooo"],list):
    print("print(coreect)")
else:
    print("wrong try again")