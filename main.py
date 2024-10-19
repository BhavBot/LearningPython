import math
age=input("Give your age now: ")
agenumber=int(age)
if agenumber<18:
    print("you cant vote ha ratio+L")
else:
    if(agenumber>=18 and agenumber<100):
        print("vote")
    else:
        print("your dead lol. gl voting if your still alive.")
print(math.sqrt(agenumber))