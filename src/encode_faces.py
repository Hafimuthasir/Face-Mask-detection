# USAGE
# python encode_faces.py --dataset dataset --encodings encodings.pickle

# import the necessary packages
# from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os
import pymysql


def enf(fn):


	imagePaths = ["static/pic/"+fn]


	knownEncodings = []
	knownNames = []

	# loop over the image paths
	for (i, imagePath) in enumerate(imagePaths):
		# extract the person name from the image path
		print("[INFO] processing image {}/{}".format(i + 1,
			len(imagePaths)))
		print("imagepath-------",imagePath)
		name = "face"
		print("id=",name)
		# load the input image and convert it from RGB (OpenCV ordering)
		# to dlib ordering (RGB)

		image = cv2.imread(imagePath)
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		# detect the (x, y)-coordnates of the bounding boxes
		# corresponding to each face in the input image
		boxes = face_recognition.face_locations(rgb,
			model='hog')

		# compute the facial embedding for the face
		encodings = face_recognition.face_encodings(rgb, boxes)

		# loop over the encodings
		for encoding in encodings:
			# add each encoding + name to our set of known names and
			# encodings
			knownEncodings.append(encoding)
			knownNames.append(name)

	# dump the facial encodings + names to disk
	print("[INFO] serializing encodings...")
	data = {"encodings": knownEncodings, "names": knownNames}
	f = open('faces.pickles', "wb")
	f.write(pickle.dumps(data))
	f.close()
	con = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='face_mask')
	cmd = con.cursor()

	cmd.execute("SELECT * FROM staff;")
	s=cmd.fetchall()
	print(s,"=================")
	for r in s:
		data = pickle.loads(open('faces.pickles', "rb").read())
		# load the input image and convert it from BGR to RGB
		image = cv2.imread("static/uploads/"+r[10])
		# print(image)
		h, w, ch = image.shape
		print(ch)
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		# detect the (x, y)-coordinates of the bounding boxes corresponding
		# to each face in the input image, then compute the facial embeddings
		# for each face
		print("[INFO] recognizing faces...")
		boxes = face_recognition.face_locations(rgb,
												model='hog')
		encodings = face_recognition.face_encodings(rgb, boxes)

		# initialize the list of names for each face detected
		names = []
		print("===================================opopop")
		# loop over the facial embeddings
		for encoding in encodings:
			# attempt to match each face in the input image to our known
			# encodings
			print("===================================opopop222222222")
			matches = face_recognition.compare_faces(data["encodings"],
													 encoding,tolerance=0.4)


			# check to see if we have found a match
			if True in matches:
				print("===================================opopopttttttttttttttt")
				# find the indexes of all matched faces then initialize a
				# dictionary to count the total number of times each face
				# was matched
				matchedIdxs = [i for (i, b) in enumerate(matches) if b]
				counts = {}

				# loop over the matched indexes and maintain a count for
				# each recognized face face
				for i in matchedIdxs:
					name = data["names"][i]
					counts[name] = counts.get(name, 0) + 1
				cmd.execute("SELECT * FROM `mask_violation` WHERE `uid`='"+str(r[1])+"' AND DATE(`date`)=CURDATE()")
				s=cmd.fetchone()
				if s is  None:
					cmd.execute("INSERT INTO `mask_violation` VALUES(NULL,now(),'" + fn + "','pending','"+str(r[1])+"')")
					con.commit()

	return "na"



def enf1(fn):


	imagePaths = ["static/cam/"+fn]


	knownEncodings = []
	knownNames = []

	# loop over the image paths
	for (i, imagePath) in enumerate(imagePaths):
		# extract the person name from the image path
		print("[INFO] processing image {}/{}".format(i + 1,
			len(imagePaths)))
		print("imagepath-------",imagePath)
		name = "face"
		print("id=",name)
		# load the input image and convert it from RGB (OpenCV ordering)
		# to dlib ordering (RGB)

		image = cv2.imread(imagePath)
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		# detect the (x, y)-coordnates of the bounding boxes
		# corresponding to each face in the input image
		boxes = face_recognition.face_locations(rgb,
			model='hog')

		# compute the facial embedding for the face
		encodings = face_recognition.face_encodings(rgb, boxes)

		# loop over the encodings
		for encoding in encodings:
			# add each encoding + name to our set of known names and
			# encodings
			knownEncodings.append(encoding)
			knownNames.append(name)

	# dump the facial encodings + names to disk
	print("[INFO] serializing encodings...")
	data = {"encodings": knownEncodings, "names": knownNames}
	f = open('faces.pickles', "wb")
	f.write(pickle.dumps(data))
	f.close()
	con = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='face_mask')
	cmd = con.cursor()

	cmd.execute("SELECT * FROM staff;")
	s=cmd.fetchall()
	print(s,"=================")
	for r in s:
		data = pickle.loads(open('faces.pickles', "rb").read())
		# load the input image and convert it from BGR to RGB
		image = cv2.imread("static/uploads/"+r[10])
		# print(image)
		h, w, ch = image.shape
		print(ch)
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		# detect the (x, y)-coordinates of the bounding boxes corresponding
		# to each face in the input image, then compute the facial embeddings
		# for each face
		print("[INFO] recognizing faces...")
		boxes = face_recognition.face_locations(rgb,
												model='hog')
		encodings = face_recognition.face_encodings(rgb, boxes)

		# initialize the list of names for each face detected
		names = []
		print("===================================opopop")
		# loop over the facial embeddings
		for encoding in encodings:
			# attempt to match each face in the input image to our known
			# encodings
			print("===================================opopop222222222")
			matches = face_recognition.compare_faces(data["encodings"],
													 encoding,tolerance=0.4)


			# check to see if we have found a match
			if True in matches:
				print("===================================opopopttttttttttttttt")
				# find the indexes of all matched faces then initialize a
				# dictionary to count the total number of times each face
				# was matched
				matchedIdxs = [i for (i, b) in enumerate(matches) if b]
				counts = {}

				# loop over the matched indexes and maintain a count for
				# each recognized face face
				for i in matchedIdxs:
					name = data["names"][i]
					counts[name] = counts.get(name, 0) + 1
				cmd.execute("SELECT * FROM `attendence` WHERE `sid`='"+str(r[1])+"' AND DATE=CURDATE()")
				s=cmd.fetchone()
				if s is  None:
					cmd.execute("INSERT INTO `attendence` VALUES(NULL,'" + str(r[1]) + "',curdate(),1)")
					con.commit()

	return "na"