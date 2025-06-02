import requests
baseurl="http://127.0.0.1:5000"

def gettasks():
    response=requests.get(f"{baseurl}/tasks")
    print("tasks: ", response.json())
    
def puttask(data):
    payload={"data":data}
    response=requests.post(f"{baseurl}/addtask", json=payload)
    
    
if __name__=="__main__":
    gettasks()
    puttask("play videogame")
    gettasks()