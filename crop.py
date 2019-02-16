import numpy as np
import cv2 as cv
import glob

for img in glob.glob("sample_output_images/*.png"):
	image = cv.imread(img)
	y = 0
	x = 0
	h = 224
	w = 224
	crop = image[y:y+h, x:x+w]
	cv.imwrite(img,crop)