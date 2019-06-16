import cv2
import numpy as np
import requests

url = "http://192.168.1.25:8080/shot.jpg"
face_cascade = cv2.CascadeClassifier("/home/bharat/Downloads/haarcascade.xml")
eye_cascade = cv2.CascadeClassifier("/home/bharat/Downloads/eye.xml")
hand_cascade = cv2.CascadeClassifier("/home/bharat/Downloads/hand.xml")
font = cv2.FONT_HERSHEY_SIMPLEX


while True:

    img = requests.get(url)
    img_arr = np.array(bytearray(img.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, 1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.05, 5)
    hands = hand_cascade.detectMultiScale(gray, 1.05, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, 'FACE', (x + int(w / 2), y), font, 1, (200, 255, 255), 2, cv2.LINE_AA)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            cv2.putText(img, 'EYE', (ex + int(ew / 2), ey), font, 1, (200, 255, 255), 2, cv2.LINE_AA)
    for (xh, yh, wh, hh) in hands:
        cv2.rectangle(img, (xh, yh), (xh + wh, yh + hh), (0, 0, 255), 2)
        cv2.putText(img, 'HAND', (xh + int(wh / 2), yh), font, 1, (200, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('img', img)

    # cv2.imshow("MobileCam", img)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()