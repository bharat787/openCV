import time

import cv2

video = cv2.VideoCapture(0)

a = 1
while True:
    check, frame = video.read()
    a = a + 1
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('capturing', frame) # instead of gray type frame for color video

    key = cv2.waitKey(1)

    if key == ord('q'):
        break
# time.sleep(3)
print(a)  # print the number of frames


# cv2.waitKey(0)

# print(check)
# print(frame)

# time.sleep(3)


video.release()

cv2.destroyAllWindows()

'''
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
#time.sleep(3)
#if vc.isOpened(): # try to get the first frame
rval, frame = vc.read()
else:
    rval = False

while rval:
cv2.imshow("preview", frame)
rval, frame = vc.read()
key = cv2.waitKey(20)
#if key == 27: # exit on ESC
#      break
#cv2.imshow(frame)
time.sleep(3)
cv2.destroyWindow("preview")
'''