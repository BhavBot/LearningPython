x=21
y=0.5
z="88"
w=int(z)
print(type(w))
r=str(y)
print(type(r))
g="3.14159"
u=float(g)
print(type(u))
print(f"w={w},y={y}")
print(22**3)
print(10**10)
if x<=20:
    print("you are less than 20 years old")
elif x>=30:
    print("you are more than 30 years old")
else:
    print("you are in the middle")
i=5
while i<=25:
    print(i)
    i=1+i
array=[0.5,0.10,0.15,0.20,0.25]
collection=["then","thine","thete","theven","thix"]
print(len(array))
print(len(collection))
print(array[4-1])
print(collection[5-1])
concatonateastring=""
for name in collection:
    concatonateastring+=name+"-"
print(concatonateastring)
family={"husband":"Anil","wife":"Amulya","son":"Bhavesh"}
print(family["husband"])
print(f"Husband is {family["husband"]} and wife is {family["wife"]} and son is {family["son"]}")
k=""
while k!="no":
    k=input("what is your fav color?")
    if k=="blue":
        print("hats very cool, my alos.")
def divides (num1,num2): #def
    if num2!=0:
        return(num1/num2)
    else:
        print("ERROR illegle move") 
value=divides (0.5,1.5)
print(value)
keys = family.keys()
print(keys)
for key in keys:
    print(family[key])