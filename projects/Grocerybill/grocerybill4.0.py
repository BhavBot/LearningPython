def input_grocery ():
    prices={}
    item=""
    while item!="exit":
        item=input("What is your item:")
        if item=="exit":
            break
        price=input(f"What is the price of {item}:")
        prices[item]=int(price)
    return prices
def print_grocerys (prices):
    print("\n\n---------Grocery bill---------\n")
    for key in prices.keys(): #is a method
        print(f"{key}: ${prices[key]}")
def get_total_price (prices):
    totalprice=0
    for price in prices.values():
        totalprice=totalprice+price
    return(totalprice)
def get_discount_price (totalprice,discountprice):
    if totalprice>=100:
        return totalprice-discountprice
    else:
        return totalprices
def main ():
    prices=input_grocery()
    print_grocerys(prices)
    totalprice=get_total_price(prices)
    print(f"\ntotal before discount: ${totalprice}")
    discountprice=80
    newtotalprice=get_discount_price(totalprice,discountprice)
    print(f"discount applied: ${discountprice}")
    print(f"final total: ${newtotalprice}")

main()
