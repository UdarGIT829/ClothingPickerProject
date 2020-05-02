#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:20:09 2020

@author: Bryan Toscano 'hyde'
"""

from garment import Garment
import jsonpickle
import csv
import os.path
from os import path

class Closet:
    def __init__(self):
        self.tops = []
        self.bottoms = []
        self.shoes = []
        
#---SIMPLE GARMENTS FUNCTIONS-------------------------------------------------#
    
    #adds a single garment. 'article' refers to article of clothing/garment
    def add(self, article):
        if article.getGarment() == 'top':
            self.tops.append(article)
        elif article.getGarment() == 'bottom':
            self.bottoms.append(article)
        elif article.getGarment() == 'shoes':
            self.shoes.append(article)
        else:
            print('Article of Clothing was not added successfully.')
    
    #removes a single garment
    def remove(self, article_type, name):
        if article_type == 'top':
            for x in self.tops:
                if x.getName() == name:
                    self.tops.remove(x)
        elif article_type == 'bottom':
            for x in self.bottoms:
                if x.getName() == name:
                    self.bottoms.remove(x)
        elif article_type == 'shoes':
            for x in self.shoes:
                if x.getName() == name:
                    self.shoes.remove(x)
        else:
            print('Article of clothing was not removed successfully.')
    
    #clears all lists
    def clear(self):
        self.tops.clear()
        self.bottoms.clear()
        self.shoes.clear()

#---FUNCTIONS THAT PRINT------------------------------------------------------#
        
    #prints all the whole closet
    def printCloset(self):
        print('Tops: ')
        for x in self.tops:
            print(x.getName())
        print('-----------')
        print('Bottoms: ')
        for x in self.bottoms:
            print(x.getName())
        print('-----------')
        print('Shoes: ')
        for x in self.shoes:
            print(x.getName())
            
    #prints all tops
    def printTops(self):
        print('Tops: ')
        for x in self.tops:
            print(x.getName())
            
    #prints all bottoms
    def printBottoms(self):
        print('Bottoms: ')
        for x in self.bottoms:
            print(x.getName())
            
    #prints all shoes
    def printShoes(self):
        print('Shoes: ')
        for x in self.shoes:
            print(x.getName())
            
#---FUNCTIONS THAT WASH---------------------------------------------------------#
            
    #Sets all garments to clean = True 
    def wash(self):
        for x in self.tops:
            x.wash()
        for x in self.bottoms:
            x.wash()
        print('All Garments have been washed.')
        
    #sets all tops to clean
    def washTops(self):
        for x in self.tops:
            x.wash()
        print('All Tops have been washed.')
        
    #sets all bottoms to clean
    def washBottoms(self):
        for x in self.bottoms:
            x.wash()
        print('All Bottoms have been washed.')
         
#---IMPORTING/EXPORTING FUNCTIONS---------------------------------------------#
    
    #will save the current closet 
    def save(self):
        data = jsonpickle.encode(self)
        file = open('mycloset.txt', 'w')
        file.write(data)
        file.close()
        print('Closet has been saved.')
        
    #will return a Closet object
    def load(self):
        if path.exists('closet.csv'):
            with open('closet.csv') as file:
                reader = csv.reader(file, delimiter=",")
                for row in reader:
                    garment = Garment(garment_type=str(row[1]), name=str(row[0]))
                    garment.changeColors(color0=row[2])
                    if(not row[3]):
                        garment.use()
                    if(garment.garment_type == "top"):
                        self.tops.append(Garment(garment))
                    if(garment.garment_type == "bottom"):
                        self.bottoms.append(Garment(garment))
                    if(garment.garment_type == "shoe"):
                        self.shoes.append(Garment(garment))
        else:
            print('Closet file does not exist!.')
