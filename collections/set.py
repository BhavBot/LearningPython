s1={1,2,3,3,3,3,1,1,1,1,1,2,2,2,2,2}
s2=set()
s2.add(245)
s1.add(24)
s2.update(s1)
s2.discard(3)
print("testing all builtinmethod: ",all(s2))
s2.add(0)
print("testing all builtinmethod: ",all(s2))
print("testing any builtinmethod: ",any(s2))
enumofs2=enumerate(s2,10000000000000)
woahlist=list(enumofs2)
print(woahlist)
for index,value in woahlist:
    print("index: ",index)
    print("value: ",value)
# comment any all and enumerate can be used on all collections including lists tuples dicts sets arrays
print(max(s2))
print(sorted(s2))
print(sum(s2))
"q9q8340973847891273489718uedub7912bwf92hqw7dny2gf2ef9u2uefc9fu2n9e7fb2u9dsfn27ge9ucjge7fcduj973wgdh9fuc3w97dgfhuc93d8g37udnff93ehfu9dnu9sxijcb279snccb8wyeggduifshncy8we9gsufhc8wyuisoghfc8xiuqsbcnxuishdc829fs8hby8edusbcsyvuhq9ushd87q9gsvyugsvcy7qgvsgfvyg7siyg7f2usg7fcy79dscg79ubxcugisbdb79qubws8diuviybasxcbg8yuw8yabgsduw7gbfgwgs7ue8gew7fusdhfuwge7fwudgsbf8igsd8ug7wedgsuf7esdgbufi87weubffg"
print(f"""yoo {s2}
yoo""")
crikgr={"virat","rohit","kohli","sharma"} # i will not use bhavesh or anil
ftblgr={"cristiano","ronaldo","kohli","virat"}
p=print #or prnt
p("union using |",crikgr|ftblgr) #you can also yous crikgr.union(ftblgr)
p("intersection using &",crikgr&ftblgr) #you can also yous crikgr.intersection(ftblgr)
p("difference using |",crikgr-ftblgr) #you can also yous crikgr.difference(ftblgr)
p("difference using |",ftblgr-crikgr) #you can also yous ftblgr.difference(crikgr)
p("symetric difference using |",crikgr^ftblgr) #you can also yous crikgr.symmetric_difference(ftblgr)
allgr=crikgr|ftblgr
if allgr.issuperset(crikgr):
    print("all group is a superset of crikgr \nbetter: conferm")
if ftblgr.issubset(allgr):
    print("ftblgr is a subset of allgr \nbetter: confermfonferm")
#pop() and remove() works justs works
allgr.difference_update(ftblgr)
print(allgr)
for c,f in zip(crikgr,ftblgr):
    print("opponets: ",c,f)

    
          











































































































































































































































































































































































































































































































































































































































































    







pass