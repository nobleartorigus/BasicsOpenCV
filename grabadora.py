import cv2

captura = cv2.VideoCapture(0)
captura.set(3,1000)
captura.set(4,700)
width , height = 1300, 700
fps = 20

fourcc = cv2.cv.CV_FOURCC("D","I","V","X")
w = cv2.VideoWriter("hola prros.avi",fourcc,fps,(width, height),1)

raw_input("picale w")

while(True):
      f, frame = capture.read()
      frame = cv2.resize(frame,(widht_height_))
      cv2.imshow("aqui el video prros",frame)
      w.write(frame)

      if(cv2.waltKey(1) & 0xFF == ord("q")):
	     break

capture.release()
w.release()
cv2.destroyAllWindows()
