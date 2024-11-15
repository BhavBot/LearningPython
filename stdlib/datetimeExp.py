# minecraftmovie 
import datetime
now=datetime.datetime.now()
print(now)
today=datetime.date.today()
print(today)
print(dir(datetime))
# timezone=datetime.timezone
# print(timezone)
# whats a class
# ahh its blue
print(datetime.time())
myfathersbd=datetime.date(1977,10,13)
print(myfathersbd)






mybd=datetime.date(2009,11,21)
print(mybd)
timstamp=datetime.date.fromtimestamp(1326244364)
print(timstamp)
print(f"current year: {today.year}")
print(f"current month: {today.month}")
print(f"current day: {today.day}")
atime=datetime.time(1,1,1,1)
print(atime)
datewithtime=datetime.datetime(1,1,1,1,1,1,1)
print(datewithtime)
# print("unix timestamp= ",datewithtime.timestamp())
difdate=mybd-myfathersbd
print("difference beteweewene my fathers date and me: ",difdate)
print(dir(difdate))
foormatieddate=mybd.strftime("%d %m %Y")
print(foormatieddate)
monthbyname=mybd.strftime("%d %b(%B) %y")
print(monthbyname)
mytime=datetime.time(1,30,12)
ampmtime=mytime.strftime("%x %p")
print(ampmtime)
# sleep is my speciality
import kgf
kgf.kgf()
kgf.yash()
inputstr=input("ENTHER DATE OF ETHER: ")
import time
# import time
# import time
myetherdate=time.strptime(inputstr,"%d %B %Y")
print(myetherdate)