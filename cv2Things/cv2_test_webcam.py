#logging allows the program to display the error and not crash.
import logging

try:
	#include cv2 for image things.
	import cv2
	#include numpy because reasons
	import numpy as np
	#include sys to use cli args. 
	import sys
	#comment
	import playsound as ps

	# get cli args and make them the file path, if you don't specify them, default to the default.
	try:
		cascPathFace = sys.argv[1]
		cascPathEyes = sys.argv[2]
		cascPathSide = sys.argv[3]
	except IndexError:
		cascPathFace = 'D:\\What\\Robot Things\\ScreamBot\\haarcascade_frontalface_default.xml'
		cascPathEyes = 'D:\\What\\Robot Things\\ScreamBot\\haarcascade_eye.xml'
		cascPathSide = 'D:\\What\\Robot Things\\ScreamBot\\haarcascade_profileface.xml'

	faceCascade = cv2.CascadeClassifier(cascPathFace)
	eyeCascade = cv2.CascadeClassifier(cascPathEyes)
	sideCascade = cv2.CascadeClassifier(cascPathSide)

	#create a VideoCapture object
	#you can specify multiple cameras with 1, 2, 3....
	#the default is 0
	cap = cv2.VideoCapture(0)

	#counter var is made
	counter = 10

	while True:

		if counter % 10 == 0:
			# Capture frame-by-frame
			# retruns True or False.
			ret, frame = cap.read()

			# convert to gray
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			## is there a face?
			faces = faceCascade.detectMultiScale(
				gray,
				scaleFactor=1.1,
				minNeighbors=5,
				minSize=(30, 30)
			)

			#eyes = eyeCascade.detectMultiScale(
			#	gray,
			#	scaleFactor=1.5,
			#	minNeighbors=8,
			#	minSize=(30, 30)
			#)
			sides = sideCascade.detectMultiScale(
				gray,
				scaleFactor=1.1,
				minNeighbors=5,
				minSize=(30, 30)
			)

			def playSound():
				pass

				




			#draw a rectange arouind any faces, as well as write a message above it. (also it can play a sound).
			for (x, y, w, h) in faces:
				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
				cv2.putText(img=frame, text='person found', org=((x), (y-5)), color=(0, 0, 255), fontFace=5, fontScale=1)
				print('Human Found!!!', counter)
				#ps.playsound('hello.mp3')
			#for (x2, y2, w2, h2) in eyes:
			#	cv2.rectangle(frame, (x2, y2), (x2+w2, y2+h2), (0, 0, 255), 1)
			for (x3, y3, w3, h3) in sides:
				cv2.rectangle(frame, (x3, y3), (x3+w3, y3+h3), (0, 0, 255), 3)
				cv2.putText(img=frame, text='person found', org=((x3), (y3-5)), color=(0, 0, 255), fontFace=5, fontScale=1)



			cv2.imshow('frame', frame)

			#if you press 'q' break.
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

	counter += 1

	#idk why.
	cap.release()
	cv2.destroyAllWindows()


#if anything goes wrong, don't crash, just display the error and prompt an input to close
except Exception as e:
	logging.error("Exception occurred", exc_info=True)
	input('...')