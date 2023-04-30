import cv2
import numpy as np

img = np.zeros((400,500, 3))

def draw(event, x,y, flags, params):
    print(event)
    if event == 1:
        cv2.circle(img, center=(x,y), radius=50, color=(255,255,0))

cv2.namedWindow(winname='window')
cv2.setMouseCallback('window', draw)

while True:
    cv2.imshow('window', img)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break
cv2.destroyAllWindows()