import cv2
import pandas as pd
from datetime import datetime

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture("image.jpg")

attendance = []

while True:

    ret, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for(x,y,w,h) in faces:

        id, conf = recognizer.predict(gray[y:y+h,x:x+w])

        if conf < 50:

            name = str(id)
            time = datetime.now().strftime("%H:%M:%S")

            attendance.append([name, time])

            cv2.putText(img,name,(x,y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.imshow("Attendance System",img)

    if cv2.waitKey(1)==13:
        break

cam.release()
cv2.destroyAllWindows()

df = pd.DataFrame(attendance, columns=["Student","Time"])

df.to_csv("attendance/attendance.csv",mode='a',index=False)
