import wrdtoimage as wti
import combine as cm
def start():
	wc=0
	with open('file.txt','r') as f:
	    for line in f:
	        for word in line.split():
			i=1
			for ltr in word:
				wti.txt_to_img(ltr,str(i))
				i=i+1
			wc=wc+1
			cm.combine(i,wc)

		
            
