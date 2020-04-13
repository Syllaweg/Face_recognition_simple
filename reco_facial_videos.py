import os 

import numpy as np
import cv2
import face_recognition as freco

video_capture = cv2.VideoCapture(0)

recup_visage = []

while True:
 # recupère le frame dans la video 
 #video_capture.read(## ADD PATH TO VIDEO###)
 ret, frame = video_capture.read()
# Convertit en RGB color, invertit, retourne le BGR capture au dessus
 rgb_frame = frame[:, :, ::-1]

# recupere les coordonnees des visage detecter dans le frames
 recup_visage = freco.face_locations(rgb_frame)


 for haut, droite, bas, gauche in recup_visage:
# Desine un carre sur chaque visage capture dans le frame
 cv2.rectangle(frame, (gauche, haut), (droite, bas), (0, 0, 255), 2)
# affiche le resultat
 cv2.imshow(‘Video’, frame)

# 'q' pour quitter
 if cv2.waitKey(1) & 0xFF == ord(‘q’):
 break


video_capture.release()
cv2.destroyAllWindows()