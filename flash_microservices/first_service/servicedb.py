from flask import Flask, jsonify, request, send_from_directory
from htmlservice import html_page
import json
from flask_cors import CORS
import sqlite3

taskspathdb=r"D:\BhavDev\Learning\flash_microservices\data\tasks.db"
app=Flask(__name__, static_folder="public")
CORS(app)
# tasks=[{"name":"nate",
#         "task":"wake up",
#         "deadline": "8 AM"},
#        {"name":"barry",
#         "task":"open portal",
#         "deadline":"2100 AD"}]

def readtasks(taskspathdb):
    connection=sqlite3.connect(taskspathdb)
    connection.row_factory=sqlite3.Row
    cursor=connection.cursor()
    cursor.execute("select * from tasks")
    rows=cursor.fetchall()
    connection.close()
    tasks=[dict(row) for row in rows]
    return tasks

tasks=readtasks(taskspathdb)

@app.route("/")
def home():
    print("hello gentlemen")
    return send_from_directory(app.static_folder, "index.html")                              # return "Doom Slayer Crudeoil"

@app.route("/tasks")
def gettasks():
    return readtasks(taskspathdb)

@app.route("/addtask", methods=["POST"])
def addtask():
    data=request.get_json()
    global tasks
    tasks.append(data["data"])
    name=data["data"].get("name")
    task=data["data"].get("task")
    deadline=data["data"].get("deadline")
    connection=sqlite3.connect(taskspathdb)
    cursor=connection.cursor()
    cursor.execute("""insert into tasks (name,task,deadline) values 
 (?, ?, ?)""", (name, task, deadline))
    connection.commit()
    connection.close()
    return jsonify({"status":"success"})

@app.route("/deletetask", methods=["POST"])
def deletetask():
    data=request.get_json()
    print("i have to delete:", data["task"])
    print(data)
    print(tasks)
    connection=sqlite3.connect(taskspathdb)
    cursor=connection.cursor()
    tasktobedel=data["task"]
    cursor.execute("""delete from tasks where task = ? """, (tasktobedel,))
    connection.commit()
    connection.close()
    return jsonify({"status":"success"})    
    
if "__main__"==__name__:
    # home()
    app.run(port=5001)