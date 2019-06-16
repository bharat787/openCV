

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("/home/bharat/Downloads/watch.jpg", 0)
resized = cv2.resize(img, (600, 1000))

cv2.imshow('img', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
plt.imshow(resized, cmap='gray', interpolation='bicubic')
plt.plot([50, 100], [80, 100], 'c', linewidth=5)
plt.show()
'''

cv2.imwrite('watchgray.png', resized)