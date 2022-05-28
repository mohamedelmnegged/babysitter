from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

import math
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("graduation-project-4b1ce-firebase-adminsdk-d9l8z-0575b351ad.json")
firebase_admin.initialize_app(cred,{'databaseURL' : 'https://graduation-project-4b1ce-default-rtdb.firebaseio.com/'})


def listener(event):
    # print(event.event_type)  # can be 'put' or 'patch'
    # print(event.path)  # relative to the reference, it seems
    # print(event.data)
    if (event.path == '/Fire'):
        # self.label_4.setText(event.data)
        fire = event.data

ref = db.reference('Sensors/')
ref.listen(listener)



app = Flask(__name__)

ll = db.reference('test/')
fire = ref.child('Fire').get()
gas = ref.child('Gas').get()
humaditiy = ref.child('Humidity').get()
temp = ref.child('Temperature').get()


@app.route('/')
def index():
    tasks = db.reference('Tasks')
    doneTasks = tasks.child('Done').get()
    unDoneTasks = tasks.child('UnDone').get()
    count = len(doneTasks[1:]) + len(unDoneTasks[1:])
    todayPoints = math.floor((100 / count) * len(doneTasks[1:]))
    points = 100
    return render_template("index.html",
                           doneTasks=doneTasks[1:],
                           unDoneTasks=unDoneTasks[1:],
                           todayPoints=todayPoints,
                           points=points, current='home')

@app.route('/games')
def games():
    return render_template('Games.html', current='games')

@app.route('/cartoon')
def cartoon():
    return render_template('Cartoon.html', current='cartoon')

@app.route('/education')
def education():
    return render_template('Education.html', current='education')

@app.route('/ajaxTasks', methods=['POST'])
def ajaxTasks():
    if request.method == 'POST':
        tasks = db.reference('Tasks/')
        doneTasks = list(tasks.child('Done').get())
        unDoneTasks = list(tasks.child('UnDone').get())
        changeTask = request.data.decode("utf-8")

        if changeTask in doneTasks:
            doneTasks.remove(changeTask)
            unDoneTasks.append(changeTask)
        else:
            unDoneTasks.remove(changeTask)
            doneTasks.append(changeTask)

        tasks.child('Done').set(doneTasks)
        tasks.child('UnDone').set(unDoneTasks)
        return 'done'

if __name__ == "__main__":
    app.run(debug= True, port=90000)