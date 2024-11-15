from colorama import Fore
from colorama import Style

def deco(color,style):
    print(f"{color}")
    if style=="italics":
        print(f"{color} \033[3m")
    if style=="bold":
        print(f"{color} \033[1m")
    if style=="underline":
        print(f"{color} \033[4m")
    x=input("text: ")
    print(x)
    print(f"{Style.RESET_ALL} \033[0m")
deco(Fore.BLUE,"italics")

def italicizeme():
    def italicizeme_func(myfunc):
        def wrapper(*args, **kwargs):
            # Call the original function and get its result
            print("\033[3m", end="")
            myfunc(*args,**kwargs)
            print("\033[0m", end="")
        return wrapper
    return italicizeme_func

def underlineme():
    def underlineme_func(myfunc):
        def wrapper(*args, **kwargs):
            # Call the original function and get its result
            print("\033[4m", end="")
            myfunc(*args,**kwargs)
            print("\033[0m", end="")
        return wrapper
    return underlineme_func

def boldme():
    def boldme_func(myfunc):
        def wrapper(*args, **kwargs):
            # Call the original function and get its result
            print("\033[1m", end="")
            myfunc(*args,**kwargs)
            print("\033[0m", end="")
        return wrapper
    return boldme_func
    
    