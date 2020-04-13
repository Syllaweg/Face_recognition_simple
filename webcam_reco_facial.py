import cv2
import sys

path_weights = "pretrained_weights/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(path_weights)

video = cv2.VideoCapture(0)

while True:
    # capture de l'image
    ret, frame = video.read()

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    visage = faceCascade.detectMultiScale( grey,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30))

    # reprend les mesures capturer par frame, 
    for (x, y, w, h) in visage:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # affiche la video
    cv2.imshow('Video', frame)

    # 'q' pour quitter la video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# fermeture de la video
video.release()
cv2.destroyAllWindows()