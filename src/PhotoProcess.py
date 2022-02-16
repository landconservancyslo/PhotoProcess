import PIL.Image
from PIL import ImageDraw, ImageFont
from tkinter import *
from tkinter import filedialog
import os
import glob

#----------------
# Define button commands
#----------------

# Select source folder
def sourceFolder():
  global sourcePath
  sourcePath = filedialog.askdirectory(initialdir="S:\\Active files\\PHOTOS")
  inputPath.insert(0, sourcePath)

#Select save folder
def destFolder():
  global destPath 
  destPath = filedialog.askdirectory(initialdir="S:\\Active files\\PHOTOS")
  outputPath.insert(0, destPath)

#Run program
def watermark():
  global sourcePath
  global destPath
  path_in = sourcePath + '\\*.jpg'
  text = textEntry.get()
  margin = 10
  font = ImageFont.truetype('arial.ttf', 36)
  for im in glob.glob(path_in):
    im_original = PIL.Image.open(im)
    im_resize = im_original.resize((960,640))
    width, height = im_resize.size
    mark = ImageDraw.Draw(im_resize)
    textwidth, textheight = mark.textsize(text, font)
    x = width - textwidth - margin
    y = height - textheight - margin
    mark.text((x,y), text, font=font)
    im_index = im.rfind('\\')
    im_name = im[(im_index + 1):]
    path_out = destPath + '\\' + im_name
    im_resize.save(path_out)
  root.destroy()    

# #Create image object from image file
# image_original = Image.open('Pic1.jpg')

# #Resize image
# image = image_original.resize((960,640))

# #Create image width/height variables for watermark placement
# width, height = image.size

# #Enable image editing
# draw = ImageDraw.Draw(image)

# #Create watermark text object
# text = '02/15/2022'

# #Create font object (font, font size)
# font = ImageFont.truetype('arial.ttf', 36)

# #Returns size of text object in pixels
# textwidth, textheight = draw.textsize(text, font)
# print(textwidth, textheight)

# #Calculate x,y coordinates of watermark based on width/height of text object 
# margin = 10
# x = width - textwidth - margin
# y = height - textheight - margin

# #Draw watermark in bottom right corner
# draw.text((x, y), text, font=font)
# image.show()

# #Save image
# image.save('Pic_date.jpg')



#---------------------
#GUI
#---------------------

# initialize root
root = Tk()

# create source path label
inputLabel = Label(root, text='Select photo folder:')
inputLabel.grid(row=0, column=0, padx=10, sticky=W)

# create text entry box for source path
inputPath = Entry(root, width=105)
inputPath.grid(row=1, column=0, padx=10, pady=20, columnspan=2, sticky=W)

# create button to select source path
selectButton_in = Button(root, text="Select", width=10, command=sourceFolder)
selectButton_in.grid(row=1, column=2, padx=10)

#create destination path label
outputLabel = Label(root, text='Select save folder:')
outputLabel.grid(row=2, column=0, padx=10, sticky=W)

#create text entry box for save path for presentation
outputPath = Entry(root, width=105)
outputPath.grid(row=3, column=0, padx=10, pady=20, columnspan=2, sticky=W)

#create button to select destination path
selectButton_out = Button(root, text="Select", width=10, command=destFolder)
selectButton_out.grid(row=3, column=2, padx=10)

# create watermark label
textLabel = Label(root, text='Enter Watermark Text:')
textLabel.grid(row=4, column=0, padx=10, sticky=W)

# create watermark entry box
textEntry = Entry(root, width=105)
textEntry.grid(row=5, column=0, padx=10, pady=20, columnspan=1, sticky=W)

# create save button
saveButton = Button(root, text="Run", width=10, command=watermark)
saveButton.grid(row=5, column=2, padx=10, pady=10)

# run mainloop
root.mainloop()





