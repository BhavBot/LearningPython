name="some name"
age=123
height=3.14
formatedstr="{}'s age is {} and height is {}"
finalstr=formatedstr.format(name,age,height)
print(finalstr)
ok={"name":"Yash",
    "age":43,
    "height":6.6}
formatedstr2="{name}'s age is {age} and height is {height}"
finalstr2=formatedstr2.format(**ok)
print(finalstr2)
ok2=["myname",2,2.0]
finalstr3=formatedstr.format(*ok2)
print(finalstr3)
#rain be like
print(1,2,3,sep="-",end=" The End",)
#87
print("using numbered parameters {1} ,{0} ,{1}".format("rohit","virat"))
print("using numbered parameters {name1} ,{name2} ,{name1}".format(name1="rohit",name2="virat"))
k=999
print("DECIMAL:{0:d}".format(k))
print("BINARY:{0:b}".format(k))
print("OCTAL:{0:o}".format(k))
print("HEXADECIMAL(lowercase):{0:x}".format(k))
print("HEXADECIMAL(UPPERCACE):{0:X}".format(k))
f=3.14159
print("FIXED 2 DECIMAL POINTS: {0:.2f}".format(f))
print("EXPONENT(lowercase): {0:e}".format(f))
print(id(f))
r="potato41"
print("LEFT ALIGN WITH SPACES: {0:^100}".format(r))
print("LEFT ALIGN WITH 0S: {0:<100}".format(r))
print("RIGHT ALIGN WITH SPACES: {0:>100}".format(r))
print("RIGHT ALIGN WITH 0S: {0:=>100}".format(r))
print("COMMA SEPERATOR: {0:,}".format(9876587654323456789))
