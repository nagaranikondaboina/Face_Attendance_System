import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)

student_id = input("Enter Student ID: ")

count = 0

while True:

    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        count += 1

        cv2.imwrite("dataset/User."+student_id+"."+str(count)+".jpg",
                    gray[y:y+h,x:x+w])

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('Capturing Face', img)

    if count >= 30:
        break

cam.release()
cv2.destroyAllWindows()
