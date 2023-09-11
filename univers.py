# -*- coding: utf-8 -*-


import numpy

class Univers():
   """to define the system. 
   Include random things and choose if other planet
   By default : no outer planets
   Travel times for locations pairs"""
   
   def __init__(self):         # class constructor
       self.earth                = 0
       self.suborbitalflight     = 1
       self.earthorbit           = 2
       self.lunarflyby           = 3
       self.lunarorbit           = 4
       self.moon                 = 5
       
       self.location = (numpy.ones((6, 6))- numpy.eye(6,6))*100
       
       self.location[self.earth, self.suborbitalflight]      = 3
       self.location[self.earth, self.earthorbit]            = 8
       self.location[self.suborbitalflight, self.earthorbit] = 5
       self.location[self.earthorbit, self.lunarflyby]       = 1
       self.location[self.earthorbit, self.lunarorbit]       = 3
       self.location[self.lunarorbit, self.moon]             = 2
       self.location[self.earthorbit, self.earth]            = 0
       self.location[self.lunarflyby, self.lunarorbit]       = 2
       self.location[self.lunarflyby, self.moon]             = 4
       self.location[self.lunarflyby, self.earthorbit]       = 1
       self.location[self.lunarorbit, self.earthorbit]       = 3
       self.location[self.moon, self.lunarorbit]             = 2
       
       
       # print(self.location)
       
       # if extension == outer planets:
           
   def position(self, name):
       	if name == "earth"       		: return   0
        if name == "suborbitalflight"   : return   1
        if name == "earthorbit"         : return   2
        if name == "lunarflyby"         : return   3
        if name == "lunarorbit"         : return   4
        if name == "moon"               : return   5








        
