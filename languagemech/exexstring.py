num=7
squarenum=eval("num*num")
print(squarenum)
prg1="""listt=[1,2,3]
for x in listt:
    print(x)"""
prg2="""hyorby=["hi","bye"]
for something in hyorby:
    print(something)"""
# program=input("enter yo program: ")
program=eval(input("program: "))
exec(program)