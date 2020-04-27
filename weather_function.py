#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 08:59:27 2020

@author: hyde
"""


import pyowm

key = pyowm.OWM('ef801b910ab8c738b5bc503ff0901571')

zipCode = input("Enter your ZipCode:  ")

observation = key.weather_at_place(zipCode)
w = observation.get_weather()
print(w.get_temperature('fahrenheit'))
print(w.get_detailed_status())
