import os
import json
current_dir = os.path.dirname(__file__)  # Get the directory of the current script
os.chdir(current_dir)

ok={"name":"me","age":"1/0","city":"beatlejuice","courses":["how to make money","doing things for fun","lol"]}


with open("./data/students.json","a",encoding="utf-8") as file:
    json.dump(ok,file,indent=4)

with open("./data/library.json","r",encoding="utf-8") as file:
    library=json.load(file)
print(library[1]["author"])
newedition={
            "year": "2024 BC",
            "formats": {
                "hardcover": {"price": 20.99, "stock": 10},
                "paperback": {"price": 19.99, "stock": 9},
                "eBook": {"price": 18.99, "stock": 8}
            }
        }
library[1]["editions"].append(newedition)
with open("./data/library.json","w",encoding="utf-8") as file:
    json.dump(library,file,indent=5)
    
    