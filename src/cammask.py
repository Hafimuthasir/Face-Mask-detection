
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
import time

cap = cv2.VideoCapture(0)

from src.detect_mask_image import mask_image



fn=''





while(True):
	try:
		ret, img = cap.read()
		# img=cv2.imread(fn)
		print(ret)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		print(len(faces))
		# for (x,y,w,h) in faces:
		# 	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #draw rectangle to main image
		emolist=[]
		cv2.imshow("Frame",img)
		if len(faces)>0:

			fn=time.strftime("%Y%m%d_%H%M%S")+".jpg"
			fn="sample.jpg"
			print(fn)
			cv2.imwrite("static/pic/"+fn,img)

			mask_image(fn)
		if cv2.waitKey(1) & 0xFF == 27:
			break
	except Exception as e:
		print(e)
		pass

