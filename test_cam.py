import numpy as np
import cv2

# param (0) pour la webcam local
video = cv2.VideoCapture(0)

while(True):

    ret, frame = video.read()

    #  filtre gris sur la video
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
    # active la webcam
    cv2.imshow('gray',gray)

    # appuyer sur 'q' pour quitter la webcam
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# ferme tout
video.release()
cv2.destroyAllWindows()