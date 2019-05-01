from PIL import ImageFont, ImageDraw, Image
import at
def txt_to_img(txt,out):
	image = Image.new('RGB', (110, 110), color = (0, 0, 0))
	fontsize = 40 

	img_fraction = 0.5

	font = ImageFont.truetype('open-sans/OpenSans-Regular.ttf', fontsize)
	#while font.getsize(txt)[0] < img_fraction*image.size[0]:
	#    fontsize += 1
	#    font = ImageFont.truetype('open-sans/OpenSans-Regular.ttf', fontsize)

	fontsize -= 1
	draw = ImageDraw.Draw(image)
	draw.text((15,15), txt,font = ImageFont.truetype('open-sans/OpenSans-Regular.ttf',fontsize), fill=(255,255,255)) 
	out="out/"+out+".png"
	image.save(out)
	at.afftrans(out)

