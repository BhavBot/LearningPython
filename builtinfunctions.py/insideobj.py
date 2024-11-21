# guts o obj

class Classesbelike:
    x=12
    y=12
    def __repr__(self):
        return f"f string {self.x},{self.y}"
        pass
    
    def add(self):
        pass
    def __yo():
        print("hmhhmhm")
C1=Classesbelike()
print(dir(C1))
dirr=filter(lambda k: not k.startswith("__"),dir(C1))
print("only me made defs: ",list(dirr))

print(hasattr(C1,"x" and "y" or "z")) # IT WORKS 
print("printing only attributes: ",vars(C1))

setattr(C1,"x",987654326890)
print(C1.x)
    
print(getattr(C1,"x"))

# knowdledge is not nolesge knowledge is noledge

# globe=globals() fractal
# print(globe)
# for something,somethingelse in globe.items():
#     print(something,somethingelse)
    
for key in list(globals().keys()):  # Use a static copy of keys
    print(f"{key}: {globals()[key]}")
    
def deff():
    define=87
    googletranslate="bad"
    print("-"*90)

    for key in list(locals().keys()):  # Use a static copy of keys
        print(f"{key}: {locals()[key]}")
deff()

inputt=input("input: ")

print(repr(C1))

print(callable(C1))

print(callable(deff))