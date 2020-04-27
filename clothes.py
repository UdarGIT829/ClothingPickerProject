#pip install pillow
from PIL import Image
import math
#center = (250,250)
#radius = 240
pastFirstGray = 75
oneIterationDark = 30
x=0
y=0


colorDict =     {'Magenta 1': [0,1], 'Magenta 2': [0,2], 'Magenta 3': [0,3],
    'Blue 1': [90,1], 'Blue 2': [90,2], 'Blue 3': [90,3],
    'Green 1': [180,1], 'Green 2': [180,2], 'Green 3': [180,3],
    'Yellow 1': [270,1], 'Yellow 2': [270,2], 'Yellow 3': [270,3]
    }#format of map will be  'name' : [degrees from 0 : number of iterations away (1-3)]

def centerXY(): # set x, y to the values of the center of the color wheel
    global x,y
    x = center[0] 
    y = center[1]

def colorPicker(): # uses the string color to set x,y to the appropriate values corresponding to the location in the color wheel
    global x,y,color,pix
    centerXY()
    colorResult = colorDict.get(color)
    if(colorResult == None):
        print("Color lookup failed")
        return
    print("X += ", (math.cos(math.radians(colorResult[0] ) )) * (pastFirstGray + colorResult[1]* oneIterationDark), "\tSin = ", math.sin(math.radians(colorResult[0] ) ) )
    x += (math.cos(math.radians(colorResult[0] ) )) * (pastFirstGray + colorResult[1]* oneIterationDark)
    y += (math.sin(math.radians(colorResult[0] ) )) * (pastFirstGray + colorResult[1]* oneIterationDark)
    return(pix[x,y])


im = Image.open('gamut.png') # Input image file, source: https://github.com/jacksongabbard/Python-Color-Gamut-Generator/blob/master/gamut.png
pix = im.load() # use pillow library to read the image into an object
center = (im.size[0]/2,im.size[1]/2) # set center to be half of width and height (500px, 500px)
print("Center of image is at: ",center)  



for color in colorDict: # loop to display the RGB values of each color
    colorPicker()
    print(color,': ',pix[x,y],'\n')
