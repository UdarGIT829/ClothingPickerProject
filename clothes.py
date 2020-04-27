#pip install pillow
from PIL import Image
import math
#center = (250,250)
#radius = 240
pastFirstGray = 75
oneIterationDark = 30
x=0
y=0

colorList = ['Magenta 1', 'Magenta 2', 'Magenta 3',
    'Blue 1', 'Blue 2', 'Blue 3',
    'Green 1', 'Green 2', 'Green 3',
    'Yellow 1', 'Yellow 2', 'Yellow 3']
#format of map will be  'name' : [degrees from 0 : number of iterations away (1-3)]
colorDict =     {'Magenta 1': [0,1], 'Magenta 2': [0,2], 'Magenta 3': [0,3],
    'Blue 1': [90,1], 'Blue 2': [90,2], 'Blue 3': [90,3],
    'Green 1': [180,1], 'Green 2': [180,2], 'Green 3': [180,3],
    'Yellow 1': [270,1], 'Yellow 2': [270,2], 'Yellow 3': [270,3]
    }
def centerXY(): # set x, y to the values of center
    global x,y
    x = center[0] 
    y = center[1]

def colorPicker():
    global x,y,color
    centerXY()
    colorResult = colorDict.get(color)
    if(colorResult == None):
        print("Color lookup failed")
        return
    print("X += ", (math.cos(math.radians(colorResult[0] ) )) * (pastFirstGray + colorResult[1]* oneIterationDark), "\tSin = ", math.sin(math.radians(colorResult[0] ) ) )
    x += (math.cos(math.radians(colorResult[0] ) )) * (pastFirstGray + colorResult[1]* oneIterationDark)
    y += (math.sin(math.radians(colorResult[0] ) )) * (pastFirstGray + colorResult[1]* oneIterationDark)

def MagentaXY(): # set x to be to the right of center, y to be at center
    global x,y
    centerXY()
    x += pastFirstGray + oneIterationDark

im = Image.open('gamut.png') # Input image file
pix = im.load()
center = (im.size[0]/2,im.size[1]/2) # set center to be half of width and height
print("Center of image is at: ",center)  


MagentaXY()
print("Set x,y to Magenta1 coords(should be 355,250): ")
print("\tX = ", x)
print("\tY = ", y)
print(pix[x,y])  # Get the RGBA Value of Magenta1 of the gamut

for color in colorDict:
    colorPicker()
    print(color,': ',pix[x,y],'\n')
