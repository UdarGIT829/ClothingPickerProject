#pip install pillow
from PIL import Image
import math
from collections import namedtuple
pastFirstGray = 75
oneIterationDark = 30
fileImported = False
# TODO: configurable variable to adjust amount of colors imported; currently ~64

#---FILE-INPUT-------------------------------------------------#
def openFile(filename):# input string, return pillow image
    im = Image.open('gamut.png') # Input image file, source: https://github.com/jacksongabbard/Python-Color-Gamut-Generator/blob/master/gamut.png
    wheel = im.load() # use pillow library to read the image into an object
    center = (250,250) # set center to be half of width and height (500px, 500px)
    fileImported = True
    maxIterDistance = (int)((center[0]-pastFirstGray)/oneIterationDark)
    print(maxIterDistance)
    return (center, wheel, maxIterDistance)

#---COLOR-DICTIONARY-CREATION-------------------------------------------------#
def colorWheelImport(center, wheel,maxIterDistance): # using  pillow image, return new color dictionary
    denominator = 16
    colorDictionary = dict()
    for numerator in range(1,33):
        print(numerator,"*PI / ",denominator)
        for distance in range(1,maxIterDistance+1):
            newLocation = (((numerator*math.pi)/(denominator)), distance) # establish x,y coords based on radial coords
            newColor = tuple(colorPicker(newLocation[0], newLocation[1],wheel)) # get (RGB) of pixel at location
            #print('\t',newColor)
            accompanyingColors = accompanyingColorPicker(newLocation, wheel,maxIterDistance)
            colorDictionary[newColor] = accompanyingColors
    return colorDictionary

#---DETERMINE ANALOGOUS COLORS-------------------------------------------------#
def accompanyingColorPicker(originalColorLocation, wheel, maxIterDistance): # return format: [1Complement, 2-3 Triad, 4-8 Shades, 7-11Analogous]
    originalTheta = originalColorLocation[0]
    originalDistance = originalColorLocation[1]
    # Complement
    complementTheta = (originalTheta + math.pi)
    complement = colorPicker(complementTheta, originalDistance,wheel)
        # Round complement to existing colors
    complement = closestColor(complement,wheel)
    # Triad
    triad1Theta = (originalTheta + ((2*math.pi)/3))
    triad2Theta = (originalTheta + ((4*math.pi)/3))
    triad1 = colorPicker(triad1Theta,originalDistance,wheel)
    triad2 = colorPicker(triad2Theta,originalDistance,wheel)
        # Round triads to existing colors
    triad1 = closestColor(triad1,wheel)
    triad2 = closestColor(triad2,wheel)
    # Shades
    shadeDistList = []
    shadeList = []
    if originalDistance == maxIterDistance:
        for counter in range(1,5):
            shadeDistList.append(originalDistance-counter)
    elif originalDistance == (maxIterDistance-1):
        for counter in range(0,4):
            shadeDistList.append(originalDistance-counter)
    elif originalDistance == 1:
        for counter in range(1,5):
            shadeDistList.append(originalDistance+counter)
    elif originalDistance == 2:
        for counter in range(0,4):
            shadeDistList.append(originalDistance+counter)
    else:
        for counter in range(-2,3):
            if(counter != 0):
                shadeDistList.append(originalDistance + counter)
    for dist in shadeDistList:
        # Round shades to closest existing colors
        shade = closestColor(colorPicker(originalTheta, dist, wheel),wheel)
        shadeList.append(shade)
    # Analogous colors
    analogousList = []
    for coneAngleDiff in range(-2,3):
        if coneAngleDiff != 0:
            newAnalogousAngle = originalTheta + coneAngleDiff * (math.pi/16)
        # Round analogous colors to closest existing colors
            analogousColor = closestColor(colorPicker(newAnalogousAngle, originalDistance, wheel),wheel)
            analogousList.append(analogousColor)
    return [complement,triad1,triad2,shadeList[0],shadeList[1],shadeList[2],shadeList[3],analogousList[0],analogousList[1],analogousList[2],analogousList[3]]

def colorPicker(radAngle, distanceIterations,wheel): # uses the string color to set x,y to the appropriate values corresponding to the location in the color wheel
    x,y = (250,250)
    cosine = math.cos(radAngle)
    sine = math.sin(radAngle)
    #print("cosine: ", cosine,"\tsine: ",sine)
    x += cosine * (pastFirstGray + distanceIterations * oneIterationDark)
    y += sine * (pastFirstGray + distanceIterations * oneIterationDark)
    #print("X = ", x, "\tY = ", y)
    return(wheel[x,y]) # the list (RGB) of the input pixel CHANGE pix to wheel

def initializeColors():
    center,wheel,maxIterDistance = openFile('gamut.png')
    colorDictionary = colorWheelImport(center, wheel,maxIterDistance)
    print(str(colorDictionary))
    return colorDictionary

def closestColor(originalColor, colorDictionary):
    difference = 766
    matchColor = originalColor
    for existingColor in colorDictionary:
        redDiff = abs(originalColor[0]-existingColor[0])
        greenDiff = abs(originalColor[1]-existingColor[1])
        blueDiff = abs(originalColor[2]-existingColor[2])
        sumDiff = redDiff + greenDiff + blueDiff
        if sumDiff < difference:
            difference = sumDiff
            matchColor = existingColor
    if matchColor == originalColor:
        print("No match found")
    return matchColor
initializeColors()

