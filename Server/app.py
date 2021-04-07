from flask import Flask, redirect, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os
import glob
import shutil
import time
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from demo import imageFunc
import schedule
import threading
from threading import Timer
from threading import Thread, Event
from flask_socketio import SocketIO, emit, send
from fixAngle import imageFuncAngle
import eventlet
from flask_mqtt import Mqtt
from celery import Celery
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SECRET_KEY'] = 'secret!'
app.config['threaded'] = True

socketio = SocketIO(app, engineio_logger=True, threaded=True, logger=True)

thread = Thread()

db = SQLAlchemy(app)


# control = False

class MonitorData(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    monitor_name = db.Column(db.String, nullable=True)
    heart_rate = db.Column(db.String, nullable=False)
    oxygen_saturation = db.Column(db.String, nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Monitor Data' + str(self.id)


num = 1


def dataRead():
    try:
        while True:
            print("my work started")
            start = time.time()
            src_dir = "static/imagesFixAngle"
            dst_dir = "static/imagesForData"
            for f in glob.iglob(os.path.join(src_dir, "*.jpg")):
                shutil.copy(f, dst=dst_dir)
            image = os.listdir('static/imagesForData')
            image = ['imagesForData/' + file for file in image]
            import subprocess
            import ast
            process = subprocess.Popen(["python", "C:\Its mine\Workspace\Flask\Demo2\demo.py"], stdout=subprocess.PIPE)
            stdout, err = process.communicate()
            Data = ast.literal_eval(stdout)
            i = 0
            # if len(Data) == 8:
            try:
                for singleImage in image:
                    name = singleImage.split('/')[1]
                    new_post = MonitorData(monitor_name=name, heart_rate=Data[i][0], oxygen_saturation=Data[i][1])
                    db.session.add(new_post)
                    db.session.commit()
                    i += 1
            except:
                print ("Data cant read")
            print(Data)  # 30 sec for raspberry pi
            end = time.time()
            print(end - start)
            time.sleep(5)
            if num == 0:
                break
    except:
        print('error')


    # if stop():
    #     break


@app.route('/')
def hello_world():
    return "Welcome To ICU Image Monitoring system"


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    pic = request.files.getlist("image[]")

    for f in pic:
        print(f)
        filename = secure_filename(f.filename)
        path = 'static/images'
        imagePath = os.path.join(path, filename)
        print(imagePath)
        # imageFuncAngle(imagePath,filename)
        f.save(imagePath)
        fixPath = 'static/imagesFixAngle'
        imageFixPath = os.path.join(fixPath, filename)
        imageFuncAngle(imageFixPath, imagePath)
    if not pic:
        return 'No pic uploaded!!', 400
    return render_template('posted.html')


@app.route('/image', methods=['GET'])
def getImage():
    mydir = 'static/imagesForData/'
    filelist = [f for f in os.listdir(mydir) if f.endswith(".jpg")]
    if filelist is not None:
        for f in filelist:
            os.remove(os.path.join(mydir, f))
    image = os.listdir('static/imagesFixAngle')
    image = ['imagesFixAngle/' + file for file in image]
    # t1 =threading.Thread(target=test_connect)
    # t2= threading.Thread(target=upload)
    # t3 = threading.Thread(target=dataRead)
    # t3.start()
    return render_template('dashboard.html', image=image)


@app.route('/heartRate')
def heartRateChart():
    return render_template('heartRate.html')

@app.route('/oxygenSaturation')
def oxygenSaturationChart():
    return render_template('oxygenSaturation.html')

@app.route('/chartData',methods=['GET'])
def chartData():
    conn = sqlite3.connect('posts.db')
    c = conn.cursor()
    # data =c.execute('SELECT * FROM (SELECT * FROM monitor_data ORDER BY date_posted DESC LIMIT 100) ORDER BY date_posted ASC ').fetchall()
    bed1 = c.execute(
        'SELECT * FROM (SELECT * FROM monitor_data WHERE monitor_name LIKE "%res0%" ORDER BY date_posted DESC LIMIT 100) ORDER BY date_posted ASC ').fetchall()
    bed2 = c.execute(
        'SELECT * FROM (SELECT * FROM monitor_data WHERE monitor_name LIKE "%res1%" ORDER BY date_posted DESC LIMIT 100) ORDER BY date_posted ASC ').fetchall()
    bed3 = c.execute(
        'SELECT * FROM (SELECT * FROM monitor_data WHERE monitor_name LIKE "%res2%" ORDER BY date_posted DESC LIMIT 100) ORDER BY date_posted ASC ').fetchall()
    bed4 = c.execute(
        'SELECT * FROM (SELECT * FROM monitor_data WHERE monitor_name LIKE "%res3%" ORDER BY date_posted DESC LIMIT 100) ORDER BY date_posted ASC ').fetchall()
    bed5 = c.execute(
        'SELECT * FROM (SELECT * FROM monitor_data WHERE monitor_name LIKE "%res4%" ORDER BY date_posted DESC LIMIT 100) ORDER BY date_posted ASC ').fetchall()
    bed6 = c.execute(
        'SELECT * FROM (SELECT * FROM monitor_data WHERE monitor_name LIKE "%res5%" ORDER BY date_posted DESC LIMIT 100) ORDER BY date_posted ASC ').fetchall()
    bed7 = c.execute(
        'SELECT * FROM (SELECT * FROM monitor_data WHERE monitor_name LIKE "%res6%" ORDER BY date_posted DESC LIMIT 100) ORDER BY date_posted ASC ').fetchall()
    bed8 = c.execute(
        'SELECT * FROM (SELECT * FROM monitor_data WHERE monitor_name LIKE "%res7%" ORDER BY date_posted DESC LIMIT 100) ORDER BY date_posted ASC ').fetchall()
    bed9 = c.execute(
        'SELECT * FROM (SELECT * FROM monitor_data WHERE monitor_name LIKE "%res8%" ORDER BY date_posted DESC LIMIT 100) ORDER BY date_posted ASC ').fetchall()
    bed10 = c.execute(
        'SELECT * FROM (SELECT * FROM monitor_data WHERE monitor_name LIKE "%res9%" ORDER BY date_posted DESC LIMIT 100) ORDER BY date_posted ASC ').fetchall()
    # data1= c.execute('SELECT * FROM (SELECT * FROM monitor_data ORDER BY date_posted DESC LIMIT 100) ORDER BY date_posted ASC ').fetchall()
    # print data
    # heart_rate= []
    # label=[]
    bed1HeartRate = []
    bed1DatePosted = []
    bed1OxygenSaturation = []
    for row in bed1:
        bed1HeartRate.append(row[2])
        bed1OxygenSaturation.append(row[3])
        bed1DatePosted.append(row[4])

    bed2HeartRate = []
    bed2DatePosted = []
    bed2OxygenSaturation = []
    for row in bed2:
        bed2HeartRate.append(row[2])
        bed2OxygenSaturation.append(row[3])
        bed2DatePosted.append(row[4])

    bed3HeartRate = []
    bed3DatePosted = []
    bed3OxygenSaturation = []
    for row in bed3:
        bed3HeartRate.append(row[2])
        bed3OxygenSaturation.append(row[3])
        bed3DatePosted.append(row[4])

    bed4HeartRate = []
    bed4DatePosted = []
    bed4OxygenSaturation = []
    for row in bed4:
        bed4HeartRate.append(row[2])
        bed4OxygenSaturation.append(row[3])
        bed4DatePosted.append(row[4])

    bed5HeartRate = []
    bed5DatePosted = []
    bed5OxygenSaturation = []
    for row in bed5:
        bed5HeartRate.append(row[2])
        bed5OxygenSaturation.append(row[3])
        bed5DatePosted.append(row[4])

    bed6HeartRate = []
    bed6DatePosted = []
    bed6OxygenSaturation = []
    for row in bed6:
        bed6HeartRate.append(row[2])
        bed6OxygenSaturation.append(row[3])
        bed6DatePosted.append(row[4])

    bed7HeartRate = []
    bed7DatePosted = []
    bed7OxygenSaturation = []
    for row in bed7:
        bed7HeartRate.append(row[2])
        bed7OxygenSaturation.append(row[3])
        bed7DatePosted.append(row[4])

    bed8HeartRate = []
    bed8DatePosted = []
    bed8OxygenSaturation = []
    for row in bed8:
        bed8HeartRate.append(row[2])
        bed8OxygenSaturation.append(row[3])
        bed8DatePosted.append(row[4])

    bed9HeartRate = []
    bed9DatePosted = []
    bed9OxygenSaturation = []
    for row in bed9:
        bed9HeartRate.append(row[2])
        bed9OxygenSaturation.append(row[3])
        bed9DatePosted.append(row[4])

    bed10HeartRate = []
    bed10DatePosted = []
    bed10OxygenSaturation = []
    for row in bed10:
        bed10HeartRate.append(row[2])
        bed10OxygenSaturation.append(row[3])
        bed10DatePosted.append(row[4])

    Data = [(bed1HeartRate, bed1OxygenSaturation, bed1DatePosted),
            (bed2HeartRate, bed2OxygenSaturation, bed2DatePosted),
            (bed3HeartRate, bed3OxygenSaturation, bed3DatePosted),
            (bed4HeartRate, bed4OxygenSaturation, bed4DatePosted),
            (bed5HeartRate, bed5OxygenSaturation, bed5DatePosted),
            (bed6HeartRate, bed6OxygenSaturation, bed6DatePosted),
            (bed7HeartRate, bed7OxygenSaturation, bed7DatePosted),
            (bed8HeartRate, bed8OxygenSaturation, bed8DatePosted),
            (bed9HeartRate, bed9OxygenSaturation, bed9DatePosted),
            (bed10HeartRate, bed10OxygenSaturation, bed10DatePosted)]

    return jsonify({'data': Data})
    # return render_template('heartRate.html',heart_rate=heart_rate,label=label)
@app.route('/greetings',methods=['GET'])
def greet():
    return jsonify({'greetings':'Its me hedayet'})

def provideDataFromDatabase():
    while True:
        # result = MonitorData.query.order_by(MonitorData.date_posted.desc()).limit(10).all()
        img1 = MonitorData.query.filter(db.or_(MonitorData.monitor_name == 'res0.jpg')).order_by(
            MonitorData.id.desc()).first()
        img2 = MonitorData.query.filter(db.or_(MonitorData.monitor_name == 'res1.jpg')).order_by(
            MonitorData.id.desc()).first()
        img3 = MonitorData.query.filter(db.or_(MonitorData.monitor_name == 'res2.jpg')).order_by(
            MonitorData.id.desc()).first()
        img4 = MonitorData.query.filter(db.or_(MonitorData.monitor_name == 'res3.jpg')).order_by(
            MonitorData.id.desc()).first()
        img5 = MonitorData.query.filter(db.or_(MonitorData.monitor_name == 'res4.jpg')).order_by(
            MonitorData.id.desc()).first()
        img6 = MonitorData.query.filter(db.or_(MonitorData.monitor_name == 'res5.jpg')).order_by(
            MonitorData.id.desc()).first()
        img7 = MonitorData.query.filter(db.or_(MonitorData.monitor_name == 'res6.jpg')).order_by(
            MonitorData.id.desc()).first()
        img8 = MonitorData.query.filter(db.or_(MonitorData.monitor_name == 'res7.jpg')).order_by(
            MonitorData.id.desc()).first()
        img9 = MonitorData.query.filter(db.or_(MonitorData.monitor_name == 'res8.jpg')).order_by(
            MonitorData.id.desc()).first()
        img10 = MonitorData.query.filter(db.or_(MonitorData.monitor_name == 'res9.jpg')).order_by(
            MonitorData.id.desc()).first()
        Data = []
        Data.append((img1.heart_rate, img1.oxygen_saturation))
        Data.append((img2.heart_rate, img2.oxygen_saturation))
        Data.append((img3.heart_rate, img3.oxygen_saturation))
        Data.append((img4.heart_rate, img4.oxygen_saturation))
        Data.append((img5.heart_rate, img5.oxygen_saturation))
        Data.append((img6.heart_rate, img6.oxygen_saturation))
        Data.append((img7.heart_rate, img7.oxygen_saturation))
        Data.append((img8.heart_rate, img8.oxygen_saturation))
        Data.append((img9.heart_rate, img9.oxygen_saturation))
        Data.append((img10.heart_rate, img10.oxygen_saturation))
        # for i in result:
        #     Data.append(((i.heart_rate), (i.oxygen_saturation)))
        # Data.reverse()
        socketio.emit('from flask', {'flask': Data}, namespace='/test')
        socketio.sleep(2)

def timeContent():
    while True:
        mainTime = time.time()
        img1time = int(mainTime-os.path.getmtime("C:\Its mine\Workspace\Flask\Demo2\static\imagesFixAngle/res0.jpg"))
        img2time = int(mainTime-os.path.getmtime("C:\Its mine\Workspace\Flask\Demo2\static\imagesFixAngle/res1.jpg"))
        img3time = int(mainTime-os.path.getmtime("C:\Its mine\Workspace\Flask\Demo2\static\imagesFixAngle/res2.jpg"))
        img4time = int(mainTime-os.path.getmtime("C:\Its mine\Workspace\Flask\Demo2\static\imagesFixAngle/res3.jpg"))
        img5time = int(mainTime-os.path.getmtime("C:\Its mine\Workspace\Flask\Demo2\static\imagesFixAngle/res4.jpg"))
        img6time = int(mainTime-os.path.getmtime("C:\Its mine\Workspace\Flask\Demo2\static\imagesFixAngle/res5.jpg"))
        img7time = int(mainTime-os.path.getmtime("C:\Its mine\Workspace\Flask\Demo2\static\imagesFixAngle/res6.jpg"))
        img8time = int(mainTime-os.path.getmtime("C:\Its mine\Workspace\Flask\Demo2\static\imagesFixAngle/res7.jpg"))
        img9time = int(mainTime-os.path.getmtime("C:\Its mine\Workspace\Flask\Demo2\static\imagesFixAngle/res8.jpg"))
        img10time = int(mainTime-os.path.getmtime("C:\Its mine\Workspace\Flask\Demo2\static\imagesFixAngle/res9.jpg"))
        timeData=[img1time,img2time,img3time,img4time,img5time,img6time,img7time,img8time,img9time,img10time]
        print(timeData)
        socketio.emit('from time',{'counting': timeData},namespace='/time')
        socketio.sleep(1)

@socketio.on('connect', namespace='/test')
def test_connect():
    global thread, num
    print('Client connected')
    num = 1
    if not thread.isAlive():
        print("Starting Thread")
        thread = socketio.start_background_task(provideDataFromDatabase)

@socketio.on('connect', namespace='/time')
def time_connect():
    print("time connected")
    global thread
    if not thread.isAlive():
        thread = socketio.start_background_task(timeContent)

@socketio.on('disconnect',namespace='/time')
def time_disconnect():
    print("time client disconnected")

# @socketio.on('disconnect', namespace='/test')
# def test_disconnect():
#     # print('Client disconnected')
#     # global num
#     # num = 0
#     print("Thread Stop because of disconnect client")


    
if __name__ == '__main__':
    # t3 = threading.Thread(target=dataRead)
    # t3.start()
    # if not control:
    #     print("main running")
    #     control = True
    # app.run(debug=False)
    # db.create_all()
    # t3 = threading.Thread(target=dataRead)
    # t3.start()
    socketio.run(app)  #off debug for single threading dataRead. If use debug dataRead threading will run twice
