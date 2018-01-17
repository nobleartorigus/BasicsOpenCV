import cv2

cap = cv2.VideoCapture(0)
cap.open(0)

while(True):

	ret,frame = cap.read()
	frame_vert= cv2.flip(frame,0)
	frame_hor = cv2.flip(frame,1)
	cv2.imshow("video perron", frame)
	cv2.imshow("vertical",frame_vert)
	cv2.imshow("horizontal",frame_hor)
	if(cv2.waitKey(1) & 0xFF == ord ("q")):
		break


cap.release()
cv2.destroyAllWindows()
