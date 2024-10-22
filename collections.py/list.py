"""yooooooooooooo
haaaa haa haa"""
#ordered
#mutable
#allow duplicatesw
#access elements by []

ar=[1,2,3,4,5,6,6]
print(ar)
ar.append(800000)
print(ar)
ar.insert(0,900000000000)
print(ar)
ar.insert(len(ar)-241,2938748)
print(ar[0])
print(ar)
ar.insert(10000000,90)
print(ar[len(ar)-1])
print(ar)
ar[1]=1298173
print(ar)
ar.pop(6)
print(ar)
#ar.clear()
print(ar)
x=ar.count(6)
print(x)
#ar.sort()
#print(ar)
#ar.sort(reverse=True)
#print(ar)\
#ar.reverse()
#print(ar)
print(ar[::-1])
#list with dict objekts
l=[{"name":"bhavesh","height":55},{"name":"akhil","height":54},{"name":"chakri","height":12}]
print(l)

def printhisheight3000(person,mylist):
    for y in mylist:
        if y["name"]==person:
            print(y["name"])
            print(y["height"])
        
printhisheight3000("akhil",l)
printhisheight3000("chakri",l)
lista=[12,23,34,45,56,67,78,89,90,]
listb=[21,32,43,54,65,76,87,98,9]
#1. create a for loop and combine them
#2. use extend method
lista.extend(listb)
print(lista)
print(listb)
#3. use + operator
listc=lista+listb
print(listc)



