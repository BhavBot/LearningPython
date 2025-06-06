from flask import Flask, jsonify, request, send_from_directory
from htmlservice import html_page
import json
from flask_cors import CORS

taskspath=r"D:\BhavDev\Learning\flash_microservices\data\tasks.json"
app=Flask(__name__, static_folder="public")
CORS(app)
# tasks=[{"name":"nate",
#         "task":"wake up",
#         "deadline": "8 AM"},
#        {"name":"barry",
#         "task":"open portal",
#         "deadline":"2100 AD"}]

def readtasks(taskspath):
    with open(taskspath, "r", encoding="utf-8") as file:
        tasks=json.load(file)
        return tasks

tasks=readtasks(taskspath)

@app.route("/")
def home():
    print("hello gentlemen")
    return send_from_directory(app.static_folder, "index.html")                              # return "Doom Slayer Crudeoil"

@app.route("/tasks")
def gettasks():
    return jsonify(tasks)

@app.route("/addtask", methods=["POST"])
def addtask():
    data=request.get_json()
    tasks.append(data["data"])
    with open(r"D:\BhavDev\Learning\flash_microservices\data\tasks.json","w",encoding="utf-8") as file:
        file.write(json.dumps(tasks, indent=2))
        file.close
    return jsonify({"status":"success"})

@app.route("/deletetask", methods=["POST"])
def deletetask():
    data=request.get_json()
    print("i have to delete:", data["task"])
    print(data)
    print(tasks)
    for task in tasks:
        if task["task"]==data["task"]:
            tasks.remove(task)
    with open(r"D:\BhavDev\Learning\flash_microservices\data\tasks.json","w",encoding="utf-8") as file:
        file.write(json.dumps(tasks, indent=2))
        file.close
        
        
        
        
    # tasks.append(data["task"])
    # with open(r"D:\BhavDev\Learning\flash_microservices\data\tasks.json","w",encoding="utf-8") as file:
    #     file.write(json.dumps(tasks, indent=2))
    #     file.close
    return jsonify({"status":"success"})
if "__main__"==__name__:
    # home()
    app.run()