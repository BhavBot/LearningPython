str1="Anaconda is fun"
print(str1.upper())
print(str1.lower())
print(str1.partition("d"))
print(str1.replace("a","u"))
print(str1.replace("a","u",1))
index=str1.find("Anil")
print("ERRORCODE: ",index)
str2="ym mane is                       "
print(len(str2))
str2=str2.rstrip()
print(len(str2))
print("SPLIT: ",str1.split(" "))
#declare an array
ar=["12","23","34"]
str3="\nkjbgfdscuybinaxmks,l.;/'d\n\n ".join(ar)
print("JOIN: ",str3)
print("STARTS WITH: ",str1.startswith("Python"))
#bruh
print("STARTS WITH: ",str1.startswith("Anaconda"))
str4="12134"
print("IS NUMERIC: ",str4.isnumeric())
index=str1.index("is")
print(index)

