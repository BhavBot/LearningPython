import sys
# first parameter is always  going to be the file name
# 2nd para will be the arguements
print("numofargs: ",len(sys.argv))
for x in range(3):
    print(f"{x + 1}: ",sys.argv[x])
