import cv2
import numpy as np

fondo = np.zeros((512,512,3),np.uint8)

longitud = 100
p1 = (200,100)
p2 = (300,100)
color = (200,200,200)
grosor = 5

p1_ = (80,20)
p2_ = (190,40)
color2 = (134,90,102)

linea = cv2.line(fondo,p1,p2,color2,grosor)

rect = cv2.rectangle(fondo,p1_,p2_,color2,grosor)

cv2.imshow("Ventana",fondo)
cv2.waitKey(0) & 0xFF
cv2.DestroyAllWindows()

