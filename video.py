import cv2

captura = cv2.VideoCapture(0)
captura.open(0)


while(captura.isOpened()):
   #Capturando frame x frame
   ret,frame = captura.read()
   gris = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   cv2.imshow(" Video prro", gris)
   if(cv2.waitKey(1) & 0xFF == ord("q")):
      break

captura.release()
cv2.destroyAllWindws()
