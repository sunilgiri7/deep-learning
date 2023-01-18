import cv2 as cv
import  numpy as np

###To read photo ###
img = cv.imread('goldfish.jpg')
cv.imshow('goldfish', img)
cv.waitKey(0)


###To read video ###
# capture = cv.VideoCapture('dog_walking.mp4')
# while True:
#     isTrue, frame=capture.read()
#     cv.imshow('video', frame)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.distroyAllWindows()