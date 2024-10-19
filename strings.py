str1="doublequoted string"
str2='singlequoted string'
str3="""Multiline
string"""
print(str1)
print(str2)
print(str3)
print("Example of indexing",str1[3])
print("Example of slicing",str1[3:9])
if str1==str2:
    print("True")
else:
    print("false")
print("example of joining 2 strings",str1+" "+str2)
for l in str1:
    print(l)
print("example of lenght of string", len(str1))
#line number 18
if "string" in str1:
    print("he is there")
str4="his name is \"anil\""
print("example of quotes in quoute",str4)
str5="my code is at c:\\mycodelocation\\"
print("example of backslashes in a string",str5)
str6="\taftertab"
print("print example of tab",str6)
str7="line1\vline2"
print("example of vertical tab",str7)
