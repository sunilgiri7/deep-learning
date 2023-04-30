import numpy as np
import cv2

img = np.zeros((450,500,3))
pt1=(100,100)
pt2=(300,300)
cv2.rectangle(img, pt1, pt2, color=(0,255, 0), thickness=1)
cv2.circle(img, center=(200,200), radius=50, color=(0,255,255))

cv2.imshow('window', img)
cv2.waitKey(0)