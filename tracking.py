import cv2
import numpy as np
import time

faces = cv2.CascadeClassifier("/home/bharat/Downloads/haarcascade.xml")

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
initSize = 36000

while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = faces.detectMultiScale(gray, 1.05, 5)
        for x, y, w, h in face:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if x<213:
                cv2.putText(img, 'RIGHT', (x, y), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
            elif 213 < x < 416:
                cv2.putText(img, 'CENTRE', (x, y), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
            else:
                cv2.putText(img, 'LEFT', (x, y), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

            print(w*h)
            print(x, x+w)

            size1 = w*h
            #time.sleep(.1)
            size2 = w*h
            if size2 < 33000:
                cv2.putText(img, 'GOING FAR', (0, 240), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
            elif 330000 < size1 < 37000:
                cv2.putText(img, 'NO CHANGE', (0, 240), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
            else:
                cv2.putText(img, 'COMING CLOSE', (0, 240), font, 1, (0, 255, 0), 2, cv2.LINE_AA)


        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break  # 27 is for escape key
print(cv2.__version__)
cap.release()
cv2.destroyAllWindows()