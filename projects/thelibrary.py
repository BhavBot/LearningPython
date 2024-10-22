library = [{
    "title": "Book Title",
    "author": "Author Name",
    "editions": [
        {
            "year": 2020,
            "formats": {
                "hardcover": {"price": 20.99, "stock": 5},
                "paperback": {"price": 12.99, "stock": 10},
                "eBook": {"price": 5.99, "stock": 100}
            }
        },
        {
            "year": 2015,
            "formats": {
                "hardcover": {"price": 18.99, "stock": 3},
                "eBook": {"price": 4.99, "stock": 200}
            }
        }
    ]
},{
    "title": "The One and Only",
    "author": "Me",
    "editions": [
        {
            "year": 2024,
            "formats": {
                "hardcover": {"price": 200.99, "stock": 1},
                "paperback": {"price": 120.99, "stock": 1},
                "eBook": {"price": 0, "stock": 1}
            }
        },
        {
            "year": 2015,
            "formats": {
                "hardcover": {"price": 18.99, "stock": 3},
                "eBook": {"price": 4.99, "stock": 200}
            }
        }
    ]
}]
def returnmenu():
    input("----------\npress enter to return")
def displaymenu():
    print("----------Library----------")
    print("1.Edit inventory")
    print("2.View inventory")
    print("----------\n3.Exit")
    action=input("\nAction: ")
    return action
def viewinv():
    for book in library:
        print(f"""Book Title: {book["title"]}
Author: {book["author"]}""")
        for edition in book["editions"]:
            print(f"""----------Stock----------
Edition/Year: {edition["year"]}""")
        for format in book["editions"][1]:
            print(f"""Hardcover: price: {book["editions"][2]} stock: {"stock"}""")
        
            
     

    returnmenu()
def editinv():
    print("----------Choose Editing----------")
    print("1.Add a book")
    print("2.Remove a book")
    print("3.Edit a book")
    editaction=input("\nEdit: ")
    return editaction
def editbook():
    print("----------Edit a book----------")
    print("1.Update stock")
    print("2.Update price")
    print("3.Update editions")
    print("4.Update author")
    print("5.Update date")
    
action=None
while action!=3:
    action=int(displaymenu())
    if action==1:
        editaction=None
        editinv()
        if editaction==1:
            addbook()
        if editaction==2:
            removebook()
        if editaction==3:
            editbook
    if action==2:
        viewinv()
    
    