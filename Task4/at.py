import cv2
import numpy as np
import random
def afftrans(in_img):
	img=cv2.imread(in_img)
	rows,cols,ch = img.shape
	pts1=np.float32([[5,5],[8,5],[5,8]])
	d1=np.float32([[6,6],[8,5],[6,9]])
	d2=np.float32([[5,5],[9,7],[6,9]])
	d3=np.float32([[6,6],[8,5],[6,9]])
	d4=np.float32([[4,7],[8,5],[7,9]])
	d5=np.float32([[5,5],[10,9],[5,8]])
	c= random.randint(1, 5)
	d={1:d1,2:d2,3:d3,4:d4,5:d5}
	pts2=d[c]
	

	#M = cv2.getAffineTransform(pts1,pts2)
	M = cv2.getAffineTransform(pts1,pts2)
	dst = cv2.warpAffine(img,M,(cols,rows))
		
	cv2.imwrite(in_img,dst)
