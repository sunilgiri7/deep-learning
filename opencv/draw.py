import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank', blank)

##Now print the image a certain colour
blank[200:300, 300:400] = 0,255,0
cv.imshow('Green', blank)

cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

# img = cv.imread('goldfish.jpg')
# cv.imshow('image', img)
cv.waitKey(0)