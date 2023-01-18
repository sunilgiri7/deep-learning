import cv2 as cv
import  numpy as np

img = cv.imread('goldfish.jpg')
cv.imshow('goldfish', img)

###Now to Resize the image ###
def rescaleframe(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

resized_image = rescaleframe(img)
cv.imshow('Image', resized_image)  

###To read video ###
capture = cv.VideoCapture('dog_walking.mp4')
while True:
    isTrue, frame=capture.read()
    frame_resized  = rescaleframe(frame)
    cv.imshow('video', frame)
    cv.imshow('video resize', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.distroyAllWindows()