import cv2 as cv
import face_recognition
vid = cv.VideoCapture(0)
image = face_recognition.load_image_file("your_file.jpg")
face_locations = face_recognition.face_locations(image)
while True:
    rat,frame = vid.read()
    cv.imshow('video', frame)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
vid.release()
cv.destroyAllWindows()