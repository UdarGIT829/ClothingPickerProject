#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:50:42 2020

@author: Bryan Toscano 'hyde'
"""

class Garment:
    
    def __init__(self, garment_type = 'shirt', name = 'def', colors = ['pri', 'sec', 'ter'], layer = 0, warmth = 0, clean = True):
        self.name = name
        self.garment_type = garment_type
        self.colors = colors
        self.tags = []
        self.layer = 0
        self.warmth = 0
        self.clean = clean


#---FUNCTIONS DEALING WITH GARMENT_TYPE---------------------------------------#
#ideally we want garments to be either 'top', 'bottom', or 'shoes'

    #changes garment type
    def changeType(self, garment_type):
        self.garment_type = garment_type
        print('Garment Type has been updated.')
        
    #prints the type of garment
    def checkGarment(self):
        print(self.garment_type)
        
    #returns the type of garment
    def getGarment(self):
        return self.garmet_type

#---FUNCTIONS DEALING WITH NAME-----------------------------------------------#
    
    #Changes name.
    def changeName(self, name):
        self.name = name
        print('Garment name has been updated.')
        
    #returns name
    def getName(self):
        return self.name

#---FUNCTIONS DEALING WITH COLOURS--------------------------------------------#
    
    #will print the 3 colors
    def checkColors(self):
        print(self.colors)
        
    #returns a list of colors
    def getColors(self):
        return self.colors
    
    #will update the colors of clothing.  Mostly used to correct user error
    def changeColors(self, color0 = "pri", color1 = "sec", color2 = "ter"):
        self.colors = [color0, color1, color2]
        print('Colors have been updated.')
        
#---FUNCTIONS DEALING WITH LAYER  --------------------------------------------#
#the bottom most layer is 0 should probaly not get higher than a 2
    
    #changes the layer value
    def changeLayer(self, layer):
        self.layer = layer
        print('Layer has been updated')
    
    #return layer
    def getLayer(self):
        return self.layer
    
#---FUNCTIONS DEALING WITH WARMTH---------------------------------------------#
#the higher the warmth the better suited a garment is for colder weather
#ideally the numbers should be from 0 - 5
        
    #changes the warmth value
    def changeWarmth(self, warmth):
        self.warmth = warmth
        print('Warmth has been update')
        
    #returns layer value
    def getWarmth(self):
        return self.warmth

#---FUNCTIONS DEALING WITH CLEAN----------------------------------------------#

    #returns and prints whether an article of clothing is clean or dirty
    def isDirty(self):
        if self.clean == True:
            print(self.name + ' is clean.')
        else:
            print(self.name + ' is dirty.')
        return self.clean
    
    #sets the clothes as usable and clean
    def wash(self):
        print(self.name + ' has been washed.')
        self.clean = True
    
    #sets the clothes as dirty and unusable without override
    def use(self):
        print(self.name + ' has been washed.')
        self.clean = False
        
#---FUNCTIONS DEALING WITH TAGS-----------------------------------------------#
    
    #will add new tags 
    def addTag(self, tags):
        self.tags.append(tags)
        print('Tag added successfully!')
      
    #will check all tags associated with garment
    def checkTag(self):
        print(self.tags)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    
