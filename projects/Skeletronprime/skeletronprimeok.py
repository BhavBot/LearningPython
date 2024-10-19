primes=[2]
#For a number to qualify as a prime number, it is not divisible by all prime number less than the number itself.
#I will add 1 to prime and check if prime, if not, add one to not prime and repeat until prim. once prime,
#add prime to primes.

def isprime(c):
    i=0
    #print("lentth of primes: ",len(primes))
    isdivbyany1=False
    while (i<len(primes)):
        if c%primes[i]==0:
            isdivbyany1=True
            #c is divisble by primes[i]
            #print("the divisor false: ",primes[i])
            #print("c false (r=0):",c)
            return False
        i+=1
    if isdivbyany1==False:
        #c is not divisible by primes[0]
        #print("returning true for c: ",c)
        return True


                                                        #i will implement it later whyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy

def adprim(p):
    primes.append(p)
def main():
    n=int(input("n: "))
    c=3
    while True:
        print(f"testing: {c}")
        if isprime(c):
            adprim(c)
        if len(primes)>=n:
            print(primes)
            break
        c+=1
main()
