import cv2
import numpy as np

img = cv2.imread("/home/bharat/Downloads/watch.jpg", 1)
resized = cv2.resize(img, (600, 1000))

cv2.line(resized, (0, 0), (150, 150), (255, 255, 255), 15)

cv2.rectangle(resized, (15, 25), (200, 150), (255, 255, 255), 5)

cv2.circle(resized, (100, 63), 55, (0, 0, 255), 15)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# pts = pts.reshape((-1,1,2))
cv2.polylines(resized, [pts], True, (0, 255, 255), 10)  # true connect final and first pt

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(resized, 'HI', (0, 130), font, 1, (200, 255, 255), 2, cv2.LINE_AA)
cv2.imshow('img', resized)

cv2.waitKey(0)

cv2.destroyAllWindows()
