# [] . ^ $ * + ? {} () \ |
import re
winrar="im 70 and my father is 40 somein and me mother is like 20 or something idk"
pattern="\d+"
result=re.findall(pattern,winrar)
print(result)
partet="\sm+[a-z]+\s"
restet=re.findall(partet,winrar)
print(restet)
reson=re.split(partet,winrar)
print(reson)
resb=re.sub(partet,"wrong",winrar)
print(resb)
redf=re.split(partet,winrar,1)
print(redf)
reb=re.sub(partet,"wrong",winrar,1)
print(reb)
resn=re.subn(partet,"wrong",winrar)
print("tuple",resn)
pson=("\Bther")
mtch=re.search(pson,winrar)
print(mtch)
# if mtch:
#     print("coreect ayyayayayayyya:",mtch.group())
#     print(mtch.group(1))
#     print(mtch.group(2))

# else:
#     print("not found:")

# Compile a pattern with ignore case and multiline flags
pattern = re.compile(r"^hello", re.IGNORECASE | re.MULTILINE)

# Test the pattern
text = """Hello there,
hello world,
HELLO everyone"""

matches = pattern.findall(text)
print(matches)

string = '\n and \r are escape sequences.'

result = re.findall(r'[\n\r]', string) 
print(result)

# Output: ['\n', '\r']