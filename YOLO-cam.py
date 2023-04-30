from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO('yolov8n.pt')
path = model('S:\Pictures\Camera Roll')
cap = cv2.VideoCapture(path)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        result = model(frame)

        annotated_frame = result[0].plot()

        cv2.imshow('webcam', annotated_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('c'):
            break
        else:
            break
cap.release()
cv2.destroyAllWindows()



