from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)
client = MongoClient("mongodb://mongo:27017/")
db = client.todo_db
tasks = db.tasks

@app.route('/')
def index():
    all_tasks = tasks.find()
    return render_template('index.html', tasks=all_tasks)

@app.route('/add', methods=['POST'])
def add():
    task_content = request.form.get('content')
    if task_content:
        tasks.insert_one({"content": task_content})
    return redirect('/')

@app.route('/delete/<task_id>')
def delete(task_id):
    tasks.delete_one({"_id": ObjectId(task_id)})
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
