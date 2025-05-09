import re

# findall(), search(), finditer(), sub()

teststring="my personal gmail address is bhavnot@gmail.com and my official email address is mediaverse@gmail.com, bhav@mediaverse.site"
emailpattern=r"[^|\s]\w+@{1}\w+\.{1}\w+\b"
emails=re.findall(emailpattern,teststring)
print(emails)

searched=re.search(emailpattern,teststring)
print(searched)
print(searched.group())

print("-"*10,"groups","-"*10)
emailpatternwithgroups=r"([^|\s]\w+)@{1}(\w+\.{1}\w+\b)"
searched=re.search(emailpatternwithgroups,teststring)
print(searched)
print("matched the entire pattern:",searched.group())
print("matched first group:",searched.group(1))
print("matched second group:",searched.group(2))

print("-"*10,"multi iter","-"*10)
for match in re.finditer(emailpattern,teststring):
    print("full match:",match.group(0))
    print(f"start and end index: {match.start()} {match.end()}")
    
def replacetext(sourcetext,replacement,start,end):
    return sourcetext[:start]+replacement+sourcetext[end:]

for match in re.finditer(emailpattern,teststring):
    sanitizedtext=replacetext(teststring, "*****", match.start(), match.end())
    print("sanitized text:",sanitizedtext)
    
print("-"*10,"substitute pattern","-"*10)
substitutedtext=re.sub(emailpattern,"*****",teststring)
print("substituted text:",substitutedtext)

    