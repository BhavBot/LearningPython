#  n u c l e a r  r e a c t o r
def gen(arg):
    avalue=0
    while avalue<arg:
        yield avalue
        avalue+=1
for v in gen(100):
    print(v)

wavelength=lambda x:[i**2 for i in gen(x)]
print(wavelength(23))
genx=(v/2 for v in wavelength(23))
for x in genx:
    print(x)

    