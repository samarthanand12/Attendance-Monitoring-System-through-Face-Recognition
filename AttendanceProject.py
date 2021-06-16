import cv2
import numpy as np
import face_recognition
import os
import joblib
from livenessmodel import get_liveness_model

import csv

from sqlite3 import *
conn = connect('record_form.db')
mycursor = conn.cursor()

try:
    mycursor.execute('select * from record limit 1')
except(OperationalError):
    #mycursor.execute("create table record(id int, name text, branch text, profession text, email text, mobile int)")
    print("please create record file first")


import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("email here", "password_here")

import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 135)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

from datetime import datetime, timedelta

check_name={}

model = get_liveness_model()
model.load_weights("model/model.h5")
print("Loaded model from disk")


process_this_frame = True
input_vid = []

# from PIL import ImageGrab

path = 'ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('Attendance.csv', 'a+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{a[name][0]},{dtString}',{a[name][1]},{a[name][2]})
            msg = "Subject: Thanking You\n\n{0}your attendance is marked".format(a[name][0])
            server.sendmail("keeptotalrecord@gmail.com", a[name][3], msg)
            engine.say("Hello, {0} your attendance is marked",a[name][0])
            engine.runAndWait()
            

def new(name):
    global check_name
    if(name not in check_name):
        print(name)
        x = datetime.now() + timedelta(seconds=30)
        x += timedelta(seconds=30)
        b = x.strftime("%H:%M:%S")
        check_name[name]=b
        with open('attendance.csv', 'a', newline='') as file:
              writer = csv.writer(file)
              now = datetime.now()
              current_date = now.strftime("%m-%d-%Y")
              current_time = now.strftime("%H:%M:%S")
              try:
                  mycursor.execute('select rec_id, name, branch, profession, email from record where rec_id={0}'.format(name))
                  for i in mycursor:
                      writer.writerow(i+(current_date, current_time))
                      engine.say("Hello, {0} your attendance is marked".format(i[1]))
                      msg = "Subject: Thanking You\n\nThank you! {0} your attendance is marked".format(i[1])
                      server.sendmail("keeptotalrecord@gmail.com", i[4], msg)
                      engine.runAndWait()
              except:
                  pass
    else:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if(current_time>check_name[name]):
            print(name)
            x = datetime.now() + timedelta(seconds=30)
            x += timedelta(seconds=30)
            b = x.strftime("%H:%M:%S")
            check_name[name]=b
            with open('attendance.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                now = datetime.now()
                current_date = now.strftime("%m-%d-%Y")
                current_time = now.strftime("%H:%M:%S")
                try:
                    mycursor.execute('select rec_id, name, branch, profession, email from record where rec_id={0}'.format(name))
                    for i in mycursor:
                        writer.writerow(i+(current_date, current_time))
                        engine.say("Hello, {0} your attendance is marked".format(i[1]))
                        msg = "Subject: Thanking You\n\nThank you! {0} your attendance is marked".format(i[1])
                        server.sendmail("keeptotalrecord@gmail.com", i[4], msg)
                        engine.runAndWait()
                except:
                    pass

              

#### FOR CAPTURING SCREEN RATHER THAN WEBCAM
# def captureScreen(bbox=(300,300,690+300,530+300)):
#     capScr = np.array(ImageGrab.grab(bbox))
#     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
#     return capScr

#encodeListKnown = findEncodings(images)
#joblib.dump(encodeListKnown, 'train_model.pkl') 

encodeListKnown = joblib.load('train_model.pkl')

print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    if len(input_vid) < 24:
        success, img = cap.read()
        imgSam = cv2.resize(img, (100,100))
        imgSam = cv2.cvtColor(imgSam, cv2.COLOR_BGR2GRAY)
        input_vid.append(imgSam)

    else:
        success, img = cap.read()
        # img = captureScreen()
        imgSam = cv2.resize(img, (100,100))
        #imgS = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        imgSam = cv2.cvtColor(imgSam, cv2.COLOR_BGR2GRAY)
        input_vid.append(imgSam)
        inp = np.array([input_vid[-24:]])
        inp = inp/255
        inp = inp.reshape(1,24,100,100,1)
        pred = model.predict(inp)
        input_vid = input_vid[-25:]
        
        if(pred[0][0]> .9):
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            
            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
            

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                name="Unknown"
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                # print(faceDis)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = classNames[matchIndex]
                    #print(name)
                    new(name)
                    #markAttendance(name)
                    
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                try:
                    mycursor.execute('select name from record where rec_id={0}'.format(name))
                    for i in mycursor:
                        cv2.putText(img, i[0], (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                except:
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        else:
            cv2.putText(img, 'WARNING!', (img.shape[1]//2, img.shape[0]//2), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)
        # Display the liveness score in top left corner   
        
        cv2.putText(img, str(pred[0][0]), (20, 20), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 0), 1)
    cv2.imshow('Webcam', img)
    if (cv2.waitKey(100) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()


