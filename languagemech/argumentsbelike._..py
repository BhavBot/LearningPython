# variable num of arg
# *args - that one is for a variable num of positional args
# **kwargs - same thing but for key words
def variposargs(*fights):
    print(*fights)
    # print(type(*fights))
    for x in fights:
        print(x)
        
variposargs(2,13,21,3,21,4,24,12,4,32,1,23,12,3,2,3,2,3)

def varikwargs(**civilwar):
    for k,v in civilwar.items():
        print(f"{k}={v}")
        
varikwargs(x="yo",y="woaah",z="its wulzy")

def both(*fights,**civilwar):
    print("unpacked fights: ",*fights)
    # unpackedcivilwar=*civilwar
    print("unpacked civilwar keys: ",*civilwar)
    print("unpacked civilwar values: ",*civilwar.values())
    varikwargs(**civilwar)

both(x="yo",y="hyo")
both(987654321234567890,x="yo",y="hyo")

# a and b can be either, c must be kwargs
def usingstar(a,b,*,c):
    print(f"using stars {a},{b},{c}")
usingstar(12,34,c="das, leo das")

# a and b must be position args, c can be either
def usingslash(a,b,/,c):                       
    print(f"using s|ash {a},{b},{c}")
usingslash(987654321111234567890,5456,98)
usingslash(a="me",b="also me",c="me^2")