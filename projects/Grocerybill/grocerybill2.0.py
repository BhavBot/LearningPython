prices={}
item1=input("item1:")
amount1=input(f"amount of {item1}:")
price1=input(f"price of each {item1}:")
totalprice1=(int(amount1)*int(price1))
prices[f"{item1}"]=f"{totalprice1}"

item2=input("item2:")
amount2=input(f"amount of {item2}:")
price2=input(f"price of each {item2}:")
totalprice2=(int(amount2)*int(price2))
prices[f"{item2}"]=f"{totalprice2}"

item3=input("item3:")
amount3=input(f"amount of {item3}:")
price3=input(f"price of each {item3}:")
totalprice3=(int(amount3)*int(price3))
prices[f"{item3}"]=f"{totalprice3}"

item4=input("item4:")
amount4=input(f"amount of {item4}:")
price4=input(f"price of each {item4}:")
totalprice4=(int(amount4)*int(price4))
prices[f"{item4}"]=f"{totalprice4}"

item5=input("item5:")
amount5=input(f"amount of {item5}:")
price5=input(f"price of each {item5}:")
totalprice5=(int(amount5)*int(price5))
prices[f"{item5}"]=f"{totalprice5}"

totalprice=((totalprice1)+(totalprice2)+(totalprice3)+(totalprice4)+(totalprice5))
if totalprice>=100:
    print(f"---------Grocery bill---------\n{item1}: ${prices[item1]}\n{item2}: ${prices[item2]}\n{item3}: ${prices[item3]}\n{item4}: ${prices[item4]}\n{item5}: ${prices[item5]}\n\ntotal before discount: ${totalprice}\ndiscount applied: $20\n\ntotal price: ${totalprice-20}\n---------End of Grocery bill---------")
else:
    print(f"---------Grocery bill---------\n{item1}: ${prices[item1]}\n{item2}: ${prices[item2]}\n{item3}: ${prices[item3]}\n{item4}: ${prices[item4]}\n{item5}: ${prices[item5]}\n\ntotal price: ${totalprice}\n---------End of Grocery bill---------")
