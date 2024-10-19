item1=input("item1:")
item2=input("item2:")
item3=input("item3:")
item4=input("item4:")
item5=input("item5:")

item1price=input(f"price of {item1}:")
item2price=input(f"price of {item2}:")
item3price=input(f"price of {item3}:")
item4price=input(f"price of {item4}:")
item5price=input(f"price of {item5}:")

totalcost=(int(item1price)+int(item2price)+int(item3price)+int(item4price)+int(item5price))
if totalcost>=50:
    discountedcost=totalcost-10
    print(f"items:{item1}:{item1price}$,{item2}:{item2price}$,{item3}:{item3price}$,{item4}:{item4price}$,{item5}:{item5price}$, total cost: {discountedcost}$   saved money: 10$")
else:
    print(f"items:{item1}:{item1price}$, {item2}:{item2price}$,{item3}:{item3price}$,{item4}:{item4price}$,{item5}:{item5price}$, total cost: {totalcost}$")
