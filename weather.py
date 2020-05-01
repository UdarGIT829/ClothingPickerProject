#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 08:59:27 2020

@author: Bryan Toscano 'hyde'
"""


import pyowm

class Weather:
    
    def __init__(self, city = 'Fullerton' , country = 'US', key = 'ef801b910ab8c738b5bc503ff0901571'):
        self.city = city
        self.country = country
        self.location = city + ', ' + country
        self.key = key
        self.owm = pyowm.OWM(key)
        self.loc = self.owm.weather_at_place(self.location)
        self.weather = self.loc.get_weather()
        self.temp = self.weather.get_temperature(unit = 'fahrenheit')
        self.fore = self.owm.three_hours_forecast(self.location)

#---FUNCTIONS THAT RETURN TODAYS'S TEMPERATURE--------------------------------#
        
    #returns the current temperature
    def currentTemp(self):
        return self.temp['temp']
    
    #returns the max temperature for today
    def maxTemp(self):
        return self.temp['temp_max']
    
    #returns the minimum temperature for today
    def minTemp(self):
        return self.temp['temp_min']

#---FUNCTIONS FOR CHECKING RAIN/SNOW------------------------------------------#
    
    #returns True if it will rain
    def rain(self):
        return self.fore.will_have_rain()
    
    #returns True if it will snow
    def snow(self):
        return self.fore.will_have_snow()
