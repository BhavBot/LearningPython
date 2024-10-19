prices={}
item=""
while item!="exit":
    item=input("What is your item:")
    if item=="exit":
        break
    price=input(f"What is the price of {item}:")
    prices[item]=int(price)
print("\n\n---------Grocery bill---------\n")
for key in prices.keys(): #is a method
    print(f"{key}: ${prices[key]}")
totalprice=0
for key in prices.keys():
    totalprice=totalprice+prices[key]
print(f"total before discount={totalprice}")
discount=20
if totalprice>= 100:
    totalprice=totalprice-discount
    print(f"discount applied: {discount}")
print(f"final total: {totalprice}")