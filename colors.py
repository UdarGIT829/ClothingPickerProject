#pip install pillow
from PIL import Image
import math
from collections import namedtuple
pastFirstGray = 75
oneIterationDark = 30
fileImported = False

def openFile(filename):# input string, return pillow image
    im = Image.open('gamut.png') # Input image file, source: https://github.com/jacksongabbard/Python-Color-Gamut-Generator/blob/master/gamut.png
    wheel = im.load() # use pillow library to read the image into an object
    center = (250,250) # set center to be half of width and height (500px, 500px)
    fileImported = True
    return (center, wheel)

def colorWheelImport(center, wheel): # using  pillow image, return new color dictionary
    denominator = 16
    colorDictionary = dict()
    for numerator in range(1,33):
        print(numerator,"*PI / ",denominator)
        for distance in range(1,4):
            newLocation = (((numerator*math.pi)/(denominator)), distance) # establish x,y coords based on radial coords
            newColor = colorPicker(newLocation[0], newLocation[1],wheel) # get (RGB) of pixel at location
            print('\t',newColor)
            accompanyingColors = accompanyingColorPicker(newLocation, wheel)
            colorDictionary[newColor] = accompanyingColors
    return colorDictionary

def accompanyingColorPicker(originalColorLocation, wheel): # format: [1Complement, 2-3 Triad, 4-8 Shades, 7-10Analogous]
    originalTheta = originalColorLocation[0]
    originalDistance = originalColorLocation[1]
    # Complement
    complementTheta = (originalTheta + math.pi)
    complement = colorPicker(complementTheta, originalDistance,wheel)
    # Triad 1
    triad1Theta = (originalTheta + ((2*math.pi )/3))
    triad2Theta = (originalTheta + ((4*math.pi)/3))
    triad1 = colorPicker(triad1Theta,originalDistance,wheel)
    triad2 = colorPicker(triad2Theta,originalDistance,wheel)
    return [complement,triad1,triad2]

def colorPicker(radAngle, distanceIterations,wheel): # uses the string color to set x,y to the appropriate values corresponding to the location in the color wheel
    x,y = (250,250)
    cosine = math.cos(radAngle)
    sine = math.sin(radAngle)
    print("cosine: ", cosine,"\tsine: ",sine)
    x += cosine * (pastFirstGray + distanceIterations * oneIterationDark)
    y += sine * (pastFirstGray + distanceIterations * oneIterationDark)
    print("X = ", x, "\tY = ", y)
    return(wheel[x,y]) # the list (RGB) of the input pixel CHANGE pix to wheel

def initializeColors():
    center,wheel = openFile('gamut.png')
    colorDictionary = colorWheelImport(center, wheel)
    print(str(colorDictionary))
    return True

initializeColors()

