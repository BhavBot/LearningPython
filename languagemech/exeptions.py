try:
    print(1/0)
except:
    print("wrong, try again.")
try:
    with open("sampleinput.txt") as file:
        content=file.read()
except:
    print("gone, reduced to atoms.")
try:
    age=9
    assert age>=18
    print("coreect.")
except AssertionError:
    print("your too young")
                                                        # height=input("height")
                                                        # if int(height)>10:
                                                        #     print("coreect")
                                                        # else:
                                                        #     print("your too short")
because={}
try:
    print("my value= because[something]",because["something"])
except KeyError:
    print("wrong try again")
    
try:
    print("my value= because[something]",because["something"])
except Exception as eroor:
    print("exeption is: ",eroor)
"inin"
list=[1,2,3]
# print(list[3])
try:
    intput=int(input("enter: "))
    v=123/intput
    s=list[3]
except EOFError:
    print("you input wrong")
except ZeroDivisionError:
    print("illigle move")
except Exception as eroor:
    print("something went wrog",eroor)
def sigma():
    s=list[3]
    
try:
    int2put=int(input("enter2: "))
    try:
        v2=123/int2put
        sigma()
    except Exception as eroo2r:
        print(f" type of exceptoin is := {type(eroo2r)} error is {eroo2r}")
       # raise ZeroDivisionError("and where did that bring you? back to me2.")
       # s=list[3]2
except EOFError:
    print("you input wrong2")
except ZeroDivisionError:
    print("illigle move2")
except Exception as eroo2r:
    print("something went wrog2: ",eroo2r)
else:
    print("say this is else")
finally:
    print("The End")
    