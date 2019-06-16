import cv2

img = cv2.imread("/home/bharat/Downloads/faces.jpg", 1 )   # reads in a imaage

face_cascade = cv2.CascadeClassifier("/home/bharat/Downloads/haarcascade.xml")

print(img)        # prints numpy array
print(img.shape)  # tells size

# cv2.imshow("face", resized)  # displays face

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

# print(type(faces))
# print(faces)

# for face detection box
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

resized = cv2.resize(img, (600, 1000))  # resize the image

cv2.imshow("Gray", resized)
cv2.waitKey(0)

cv2.destroyAllWindows()