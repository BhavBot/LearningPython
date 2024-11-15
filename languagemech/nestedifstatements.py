year=input("year: ")
year=int(year)
if year%4==0:
    if year%100!=0:
        print("this may be a leap year.")
    elif year%100==0:
        if year%400==0:
            print("this may be a leap year.")
        else:
            print("probaly not a leap year.")
    else:
        print("probaly not a leap year.")
else:
    print("probaly not a leap year.")




