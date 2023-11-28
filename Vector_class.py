#!/usr/bin/env python
import math as m
'''
This class contains functions to store and evaluate operations for a vector 

Questions: anhellesnes@fhs.mil.no
'''

class Vector:
    '''Class for containing Vector object with magnitude and angle'''
    def __init__(self, magnitude = 0.0, angle = 0.0):
        '''Initialise obbject with magnitude and angle

        Args:
            magnitude: Float value of vector magnitude, 0.0 by default
            angle: Float value of vector magnituce, 0.0 by default
        '''
        self.magnitude = 0.0
        self.angle = 0.0
        if isinstance(magnitude, tuple) or isinstance(magnitude,list): #failsafes - trengs nok ikke
            angle = magnitude[1]
            magnitude = magnitude[0] 
            
        elif isinstance(magnitude, Vector): # same - failsafes
            angle = magnitude.angle
            magnitude = magnitude.magnitude
            

        self.set(magnitude, angle)

    def set(self, vector_magnitude, vector_angle):
        '''Simple set helper class to change value of vector

        args:
            vector_magnitude: Float value of vector magnitude
            vector_angle: Float value of vector angle
        '''
        self.magnitude = vector_magnitude
        self.angle = vector_angle

    def __add__(self, other): 
        '''Helper function for use of + (addition)  with vector objects'''
        if isinstance(other, Vector):
            #return Vector(self.magnitude + other.magnitude, self.angle + other.angle)
           return Vector(m.sqrt(m.pow(self.magnitude,2)+m.pow(other.magnitude,2)+2*self.magnitude*other.magnitude*m.cos(m.radians(other.angle)-m.radians(self.angle))),self.angle + m.degrees(m.atan2(other.magnitude*m.sin(m.radians(other.angle)-m.radians(self.angle)),self.magnitude+other.magnitude*m.cos(m.radians(other.angle)-m.radians(self.angle)))))
        elif isinstance(other, int) or isinstance(other, float):
            #return Vector(self.magnitude + other, self.angle + other)
            return Vector(m.sqrt(m.pow(self.magnitude,2)+m.pow(other.magnitude,2)+2*self.magnitude*other.magnitude*m.cos(m.radians(other.angle)-m.radians(self.angle))),self.angle + m.degrees(m.atan2(other.magnitude*m.sin(m.radians(other.angle)-m.radians(self.angle)),self.magnitude+other.magnitude*m.cos(m.radians(other.angle)-m.radians(self.angle)))))
        else:
            return NotImplemented

    def __iadd__(self, other): 
        '''Helper function for use of += (addition with self and other) with vector objects'''
        if isinstance(other, Vector):
            #return Vector(self.magnitude + other.magnitude, self.angle + other.angle)
            return Vector(m.sqrt(m.pow(self.magnitude,2)+m.pow(other.magnitude,2)+2*self.magnitude*other.magnitude*m.cos(m.radians(other.angle)-m.radians(self.angle))),self.angle + m.degrees(m.atan2(other.magnitude*m.sin(m.radians(other.angle)-m.radians(self.angle)),self.magnitude+other.magnitude*m.cos(m.radians(other.angle)-m.radians(self.angle)))))
        elif isinstance(other, int) or isinstance(other, float):
            #return Vector(self.magnitude + other, self.angle + other)
            return Vector(m.sqrt(m.pow(self.magnitude,2)+m.pow(other.magnitude,2)+2*self.magnitude*other.magnitude*m.cos(m.radians(other.angle)-m.radians(self.angle))),self.angle + m.degrees(m.atan2(other.magnitude*m.sin(m.radians(other.angle)-m.radians(self.angle)),self.magnitude+other.magnitude*m.cos(m.radians(other.angle)-m.radians(self.angle)))))
        else:
            return NotImplemented
        
    def __sub__(self, other): 
        '''Helper function for use of - (subtraction) with vector objects'''
        if isinstance(other, Vector):
            return Vector(self.magnitude - other.magnitude, self.angle - other.angle)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.magnitude - other, self.angle - other)
        else:
            return NotImplemented

    def __mul__(self, other):
        '''Helper function for use of * (multiplication) with vector objects'''
        if isinstance(other, Vector):
            return Vector(self.magnitude * other.magnitude, self.angle * other.angle)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.magnitude * other, self.angle) # Her har jeg fjernet gangingen av angle fra forrige koden fordi dette gir ikke mening matematisk
        else:
            return NotImplemented

    def __truediv__(self, other):
        '''Helper function for use of / (division without rounding or flooring) with vector objects'''
        if isinstance(other, Vector):
            return Vector(self.magnitude / other.magnitude, self.angle / other.angle)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.magnitude / other, self.angle / other)
        else:
            return NotImplemented

    def showVector(self):
        '''Helper to print magnitude and angle of self rounded of to 3 decimals'''
        print ("Magnitude: " , round(self.magnitude, 3) , " Angle: " , round(self.angle, 3))