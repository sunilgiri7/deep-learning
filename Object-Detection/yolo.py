import argparse
import time
import cv2
import os
import numpy as np

# Define the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections, IoU threshold")
ap.add_argument("-t", "--threshold", type=float, default=0.3,
	help="threshold when applying non-maxima suppression")
args = vars(ap.parse_args())

labels_path = open('coco.names').read()
labels = labels_path.strip().split('\n')

#initilize list of colors to represent each possible class label
COLORS = np.random.randint(0,255, size=(len(labels), 3), dtype='uint8')

# path to yolo weights and config path

weights = 'yolov3.weights'
config_path = 'yolov3.cfg'

net = cv2.dnn.readNetFromDarknet(config_path, weights)

# load input image

image = cv2.imread(args['image'])
(H, W) = image.shape[:2]

# determine output layer names that we need from YOLO
ln = net.getLayerNames()
ln = [ln[int(i) - 1] for i in net.getUnconnectedOutLayers()]

# construct blob from input image and then perform a forward

blob = cv2.dnn.blobFromImage(image, 1/255.0, (255,255), swapRB=True, crop=False)
net.setInput(blob)
layerOutput = net.forward(ln)

# now creating list for bounding box in image
boxes = []
confidences = []
classIDs = []

for output in layerOutput:
    for detection in output:
        score = detection[5:]
        classID = np.argmax(score)
        confidence = score[classID]
        
        if  confidence > args['confidence']:
            box = detection[0:4] * np.array([W,H,W,H])
            (centerX, centerY, width, height) = box.astype('int')
            
            x = int(centerX - (width / 2))
            y = int(centerY - (height / 2))
            
            boxes.append([x,y, int(width), int(height)])
            confidences.append(float(confidence))
            classIDs.append(classID)
            
idxs = cv2.dnn.NMSBoxes(boxes, confidences, args['confidence'],
                       args['threshold'])

if len(idxs) > 0:
    for i in idxs.flatten():
        (x, y) = (boxes[i][0], boxes[i][1])
        (w, h) = (boxes[i][2], boxes[i][3])
        
        color = [int(c) for c in COLORS[classIDs[i]]]
        cv2.rectangle(image, (x,y), (x+w, y+h), color, 2)
        text = "{}: {:.4f}".format(labels[classIDs[i]], confidences[i])
        cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
            0.5, color, 2)
        
cv2.imshow("Image", image)
cv2.waitKey(0)