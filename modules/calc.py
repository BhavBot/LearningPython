def add(n,m):
    print(n+m)
    return n+m
def mine(n,m):
    print(n-m)
    return n-m
print("calc.py: the name of my module is: ",__name__)
if __name__=="__main__":
    print("this is my test code whcih will not run if i include this as a module:","this is my realm")
    