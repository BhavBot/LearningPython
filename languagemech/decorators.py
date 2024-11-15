#  y o o o o o o o o
# decorator is a function wrapper
# or is it a rapper?
# the outer function is called the decorator which takes the original function as an argument and returns a modified version
import colorama
from colorama import Fore
from colorama import Style

print(f"{Fore.BLUE}yuoooooooooooooooo{Style.RESET_ALL}")
def function():
    print("function")
    
def function2():
    print("venom")
    
def outer(myfunction):
    def inner():
        print("Decorating before")
        myfunction()   
        print("Decorating after") 
    print("innerfunctionion =",id(inner))     # label
    return inner

mydecoratedfunction=outer(function)
print("my decorated function =",id(mydecoratedfunction))
mydecoratedfunction()

x2=outer(function2)
print("x2 =",id(x2))
x2()
# def colorizeme(myfunc,color):
#     def inner():
#         print(f"{color}")
#         myfunc()
#         print(f"{Style.RESET_ALL}")
#     return inner
# # colorizedfunc2=colorizeme(function2)
# # colorizedfunc2()
    
# @colorizeme(function2,Fore.BLUE)    
# def tobedec():
#     print("lets see if i will decorate it")

# tobedec()

    
def colorizeme(color):
    def colorizeme_func(myfunc):
        def wrapper(*args, **kwargs):
            # Call the original function and get its result
            print(f"{color}")
            myfunc(args,kwargs)
            print(f"{Style.RESET_ALL}")
        return wrapper
    return colorizeme_func

def italicizeme():
    def italicizeme_func(myfunc):
        def wrapper(*args, **kwargs):
            # Call the original function and get its result
            print(f"\033[3m")
            myfunc(args,kwargs)
            print(f"\033[0m")
        return wrapper
    return italicizeme_func

def underlineme():
    def underlineme_func(myfunc):
        def wrapper(*args, **kwargs):
            # Call the original function and get its result
            print(f"\033[4m")
            myfunc(args,kwargs)
            print(f"\033[0m")
        return wrapper
    return underlineme_func

def boldme():
    def boldme_func(myfunc):
        def wrapper(*args, **kwargs):
            # Call the original function and get its result
            print(f"\033[1m")
            myfunc(args,kwargs)
            print(f"\033[0m")
        return wrapper
    return boldme_func

@italicizeme()
@colorizeme(Fore.BLUE)
def myfunction():
    print("something")
@underlineme()
@colorizeme(Fore.RED)    

def newprint():
    print("anything")
    input1=input("input: ")
    print(input1)
    
@boldme()
@colorizeme(Fore.MAGENTA)
def print_bm(*args,**kwargs):
    print(args,kwargs,end="")

@italicizeme()
@colorizeme(Fore.LIGHTGREEN_EX)
def print_ilg(*args,**kwargs):
    print(args,kwargs,end="")
print_bm("yo tsup")

print_ilg("ipl")
newprint()

myfunction()                                                # def venom():
                                                #     color=input("input: ")
                                                #     text=input("")
                                                #     print(str(colorizeme(color)))
                                                # Call the function


    























                                                        # def yo():
                                                        #     num1=input("input: ")
                                                        #     num2=input("input: ")
                                                        #     return num1,num2
                                                        # yen=yo()
                                                        # print(yen[0])
                                                        # print(yen[1])

