import cv2
import numpy as np

img = cv2.imread("/home/bharat/Downloads/watch.jpg", 1)
resized = cv2.resize(img, (600, 1000))

'''
resized[55, 55] = [255, 255, 255]
px = resized[55, 55]
print(px)
'''

watch_face = resized[37:111, 107:194]
resized[0:74, 0:87] = watch_face


cv2.imshow('im', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()