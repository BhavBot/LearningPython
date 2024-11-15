import polymorphism as poly
chops=poly.childrenchops()
# for cutout in chops:
#     print(cutout.area())
area=[]   
for cutout in chops:
    area.append(cutout.area())
print(sum(area))
Total=0
for cutout in chops:
    Total+=cutout.area()
print(Total)
p