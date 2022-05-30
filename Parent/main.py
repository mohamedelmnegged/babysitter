from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import os
import math
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("graduation-project-4b1ce-firebase-adminsdk-d9l8z-0575b351ad.json")
firebase_admin.initialize_app(cred,{'databaseURL' : 'https://graduation-project-4b1ce-default-rtdb.firebaseio.com/'})


# def listener(event):
#     # print(event.event_type)  # can be 'put' or 'patch'
#     # print(event.path)  # relative to the reference, it seems
#     # print(event.data)
#     if (event.path == '/Fire'):
#         # self.label_4.setText(event.data)
#         fire = event.data

#ref.listen(listener)


app = Flask(__name__)


@app.route('/')
def index():
    if auth() == "true":
        ref = db.reference('Sensors/')
        fire = ref.child('Fire').get()
        gas = ref.child('Gas').get()
        humaditiy = ref.child('Humidity').get()
        temp = ref.child('Temperature').get()

        tasks = db.reference('Tasks/')
        unDoneTasks = list(tasks.child('UnDone').get())[1:]

        return render_template('index.html',
                               fire=fire,
                               gas=gas,
                               temp=temp,
                               humaditiy=humaditiy,
                               unDoneTasks=unDoneTasks)
    else:
        return redirect('/login')

@app.route('/logout')
def logout():
    if os.environ.get('auth') == "true":
        del os.environ['auth']
    return "logged out "

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/doLogin', methods=['POST'])
def doLogin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        auth = db.reference('Auth/')
        authEmail = auth.child('Email').get()
        authPass  = auth.child('Pass').get()

        if email == authEmail and password == authPass:

            os.environ['auth'] = "true"
            return redirect('/')
    return redirect('/login')


@app.route('/ajaxTasks', methods=['POST'])
def ajaxTasks():
    if request.method == 'POST':
        tasks = db.reference('Tasks/')
        unDoneTasks = list(tasks.child('UnDone').get())
        newTask = request.data.decode("utf-8")
        unDoneTasks.append(newTask)
        tasks.child('UnDone').set(unDoneTasks)
        return 'done'

def auth():
    return os.environ.get('auth')



if __name__ == "__main__":
    app.run(debug= True, port=90000)