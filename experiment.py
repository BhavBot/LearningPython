str1=input("input: ")
arrayNums=str1.split(",")
print(arrayNums)
print(type(arrayNums[1]))

array2=[]
for k in arrayNums:
    array2.append(int(k))
print(array2)
total=0
for i in array2:
    total+=i
print("total=",total)
    
avg1=total/len(array2)
print("avg=",avg1)
max1=max(array2)
print("max=",max1)

stud={"bhavesh":[20,20,30],"andy":[20,30,10],"Rakesh":[100,100,100],
"goliath":[200,300,400],"PheonixSC":[4,3,8]}
print(stud)
del stud["andy"]
print(stud)

studavg={}
for s in stud:
    sum1=sum(stud[s])
    avg1=sum1/len(stud[s])
    print(avg1)
    print(s)
    studavg[s]=avg1
print("stud avgs=",studavg)
beststud=""
maxavg=0
for g in studavg:
    if studavg[g]>maxavg:
        newmaxavg=studavg[g]
        maxavg=newmaxavg
        beststud=g
print(f"beststud is {beststud} and score is {maxavg}")





    