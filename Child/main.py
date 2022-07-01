from flask import Flask
from flask import  render_template, request, redirect, url_for

import math
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import urllib
import simplejson

from bs4 import BeautifulSoup
import requests

from pytube import YouTube

#cred = credentials.Certificate("graduation-project-4b1ce-firebase-adminsdk-d9l8z-0575b351ad.json")
#firebase_admin.initialize_app(cred,{'databaseURL' : 'https://graduation-project-4b1ce-default-rtdb.firebaseio.com/'})

cred = credentials.Certificate("esp-firebase-demo-bc7a1-firebase-adminsdk-b3ta2-f5c655842c.json")
firebase_admin.initialize_app(cred,{'databaseURL' : 'https://esp-firebase-demo-bc7a1-default-rtdb.firebaseio.com/'})


# def listener(event):
#     # print(event.event_type)  # can be 'put' or 'patch'
#     # print(event.path)  # relative to the reference, it seems
#     # print(event.data)
#     if (event.path == '/Fire'):
#         # self.label_4.setText(event.data)
#         # fire = event.data
#         print('fire')


app = Flask(__name__)

ref = db.reference('Sensors/')
#ref.listen(listener)

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
    cartoon = db.reference('Videos').child("Cartoon").get()
    videos = []
    for video in cartoon[1:]:
        yt = YouTube(video)
        print(yt.title)
        videos.append([yt.title, video])
    
    return render_template('Cartoon.html',
                           current='cartoon', 
                           videos=videos)

@app.route('/education')
def education():
    education = db.reference('Videos').child("Education").get()
    videos = []
    for video in education[1:]:
        yt = YouTube(video)
        print(yt.title)
        videos.append([yt.title, video])
    
    return render_template('Education.html', 
                            current='education',
                            videos=videos)

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