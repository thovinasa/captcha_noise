import cv2
import numpy as np
import random
from scipy import misc
def combine(inp,out):
	i=1
	for i in range(1,inp-1):
		im1="out/"+str(i)+".png"
		im2="out/"+str(i+1)+".png"
		img1=cv2.imread(im1)
		img2=cv2.imread(im2)
		vis=np.concatenate((img1,img2),axis=1)
		cv2.imwrite(im2,vis)
	oimg="captchaout/"+str(out)+".png"

	x1=random.randint(1,150)
	y1=random.randint(1,99)
	x2=random.randint(250,400)
	y2=random.randint(1,99)
	'''d=random.randint(20,50)
	c=random.randint(1,10)
		x2=x1+d
		y2=y1+c'''
	cv2.line(vis,(x1,y1),(x2,y2),(255,255,252),2)
	c=random.randint(1,5)		
	if(c==2):
		vis=~vis
	elif(c==3):
		vis=-vis
		cv2.line(vis,(x1,y1),(x2,y2),(255,255,252),2)		
	
	cv2.GaussianBlur(vis,(5,5),0)
	cv2.imwrite(oimg,vis)
	

# 0. Read the image
	image  = misc.imread(oimg,mode="L")

# 1. Add noises to the image
	noisy1 = image + image.std() * np.random.random(image.shape)
	cv2.imwrite(oimg,noisy1)
	print oimg



		
	
