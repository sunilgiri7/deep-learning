import cv2
import numpy as np

img = np.zeros((400,500,3))
flag=False
click=-1
move=-1

def draw(event, x, y, flags, params):
    print(event)
    global flag, click, move

    if event == 1: # event is nothing but when we touch img
        flag=True # if even is 1 then only flag gonna true
        click = x
        move = y
    if event == 0: # when cruser go through img then its 0
        if flag==True:
            cv2.rectangle(img, pt1=(click, move), pt2=(x, y), color=(255,0,0))

    elif  event == 4: # after touch on window its 4
        flag=False
        cv2.rectangle(img, pt1=(click, move), pt2=(x, y), color=(255,0,0))

cv2.namedWindow(winname='window')
cv2.setMouseCallback('window', draw)

while True:
    cv2.imshow('window', img)
    
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break
cv2.destroyAllWindows()