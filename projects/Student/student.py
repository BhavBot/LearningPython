studentgrades={}
gradeavgs={}
def displaymenu():
    print("----------Menu----------\n1.Add a student and their grades\n2.Remove a student\n3.View all students and their average grades\n4.Find the highest scoring student\n5.Exit the program")
    action=input("Choose action num:")
    if action.isnumeric():
        return action
    else:
        print("WRONG TRY AGAIN")
        returnmenu()
def returnmenu():
    action=input("----------\npress enter to return to menu")
    if action=="":
        print("")
def addstud():
    total=0
    student=input("----------\nStudent name:")
    grades=input("Student grades:")
    studentgrades[student]=grades.split(",")
    for grades in studentgrades[student]:
        g=int(grades)
        total+=g
        avg=total/len(studentgrades[student])
        gradeavgs[student]=avg
    print(gradeavgs)
    print(studentgrades)
    print("\033[32m----------\nStudent added\033[0m")
def delstud():
    removestud=input("----------\nStudent name:")
    if removestud in studentgrades:
        confdel=input(f"Confirm to remove {removestud} (type yes or no):")
        if confdel=="yes":
            del(studentgrades[removestud])
            print(f"{removestud} has been removed")
        elif confdel=="no":
            print("confirmation denied")
    elif removestud not in studentgrades:
        print(f"{removestud} does not exist")
def viewstuds():
    print("----------Students----------")
    for stud in studentgrades:
            print("Name:",stud,"\nMarks:",studentgrades[stud],"\nAverage:",gradeavgs[stud],"\n")
def topper():
    beststud=""
    maxavg=0
    for g in gradeavgs:
        if gradeavgs[g]>maxavg:
            newmaxavg=gradeavgs[g]
            maxavg=newmaxavg
            beststud=g
    print(f"----------\nTopper is: {beststud}\nwith average marks of: {maxavg}")
action=None
while action!=5:
    action=int(displaymenu())
    if action==1:
        addstud()
        returnmenu()
    if action==2:
        delstud()
        returnmenu()
    if action==3:
        viewstuds()
        returnmenu()
    if action==4:
        topper()
        returnmenu()
    


    
        
 
