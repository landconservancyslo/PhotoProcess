from PIL import Image, ImageDraw, ImageFont

#Create image object from image file
image_original = Image.open('Pic1.jpg')

#Resize image
image = image_original.resize((960,640))

#Create image width/height variables for watermark placement
width, height = image.size

#Enable image editing
draw = ImageDraw.Draw(image)

#Create watermark text variable
text = '02/15/2022'

#Create font variable (font, font size)
font = ImageFont.truetype('arial.ttf', 36)

#Not sure what this does
textwidth, textheight = draw.textsize(text, font)

#Calculate x,y coordinates of watermark
margin = 10
x = width - textwidth - margin
y = height - textheight - margin

#Draw watermark in bottom right corner
draw.text((x, y), text, font=font)
image.show()

#Save image
image.save('Pic_date.jpg')





