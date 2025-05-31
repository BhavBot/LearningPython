"""
creates a document.
1. create
creates a document like like eh eheheeh ehe employee or user
uses http POST

2. read
reads an existing document
uses http GET

3.update
updates an existing document with details
uses http PUT (many times even POST is used)

4. delete
deletes an existing document
uses http DELETE
"""

import requests
# BASEURL = "https://reqres.in/api/users"

# def createuser(name,job,ipdress):
#     data={"name":name,"job":job,"ipdress":ipdress}
#     response=requests.post(BASEURL,json=data)
#     if response.status_code==201:
#         print("user created")
#         print(response.json())
#         return response.json().id
#     else:
#         print("failed to create user")
#         print(response.text)

# def readuser(userid):
#     response=requests.get(f"{BASEURL}/{userid}")
#     if response.status_code==200:
#         print("user details")
#         print(response.json())
#     else:
#         print("userid not found")

BASE_URL = "https://fakestoreapi.com/products"

def create_product(title, price, description, category, image):
    """Create a new product."""
    data = {
        "title": title,
        "price": price,
        "description": description,
        "category": category,
        "image": image
    }
    response = requests.post(BASE_URL, json=data)
    if response.status_code == 200 or response.status_code == 201:
        print("Product created:", response.json())
    else:
        print("Failed to create product:", response.text)


def get_product(product_id):
    """Get product details by ID."""
    response = requests.get(f"{BASE_URL}/{product_id}")
    if response.status_code == 200:
        print("Product details:", response.json())
    else:
        print(f"Product with ID {product_id} not found.")
if __name__=="__main__":
    # id=createuser("john wick","dog avenger",1234431)
    
    # readuser(id)
    
    # Create a product
    # create_product(
    #     title="magturn",
    #     price=199.99,
    #     description="toy spins be like saturn educational space astronomy childrens toys 1 year 2 year 10 year 20 year",
    #     category="educational",
    #     image="https://via.placeholder.com/150"
    # )

    # Get details of a product
    get_product(21)  # Product ID 1 exists in the FakeStoreAPI
    