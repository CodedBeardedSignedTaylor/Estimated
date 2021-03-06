'''
Created on Sep 14, 2014

@author: Taylor
'''
from CA01.prod.Component import Component
from math import sqrt, ceil, exp, log

class Repository(object):

    def __init__(self, capacity=100):
        if(isinstance(capacity, int) and capacity > 0):
            self.capacity = capacity
            self.components = []
            self.componentCount = 0
        else:
            raise ValueError("Repository.__init__:")
    
    def addComponent(self, component=None):
        if (isinstance(component, Component)):
            if(len(self.components) == self.capacity):
                self.components.pop(0)
            self.components.append(component)
            self.componentCount = len(self.components)
            return len(self.components)
        else:
            raise ValueError("Repository.addComponent: you didn't provide a Component.") 
    
    def count(self):
        return self.componentCount
    
    def validCount(self):
        vc = 0
        for comp in self.components:
            if(comp.getMethodCount() > 0):
                vc += 1
        return vc 
    
    def determineRelativeSizes(self):
        if (self.validCount() < 2):
            raise ValueError ("Repository.determineRelativeSizes:")
        nSizes = self.calculateNormalizedSizes()
        avg = self.calculateAverage(nSizes)
        std = self.calculateStdDeviation(avg, nSizes)
        
        verySmall = int(ceil(exp(avg - (2 * std))))
        small = int(ceil(exp(avg - std)))
        medium = int(ceil(exp(avg)))
        large = int(ceil(exp(avg + std)))
        veryLarge = int(ceil(exp(avg + (2 * std))))
        return [verySmall, small, medium, large, veryLarge]
        
    def calculateNormalizedSizes(self):
        normalizedSizes = []
        for comp in self.components:
            if(comp.getMethodCount() > 0):
                loc = float(comp.getLocCount())
                meth = float(comp.getMethodCount())
                a = float(loc / meth)
                b = abs(log(a))
                normalizedSizes.append(b)
        return normalizedSizes
        
    def calculateAverage(self, normalized):
        s = 0
        for num in normalized:
            s += num
        return (s / len(normalized))
    
    def calculateStdDeviation(self, avg, nSizes):
        a = 0
        b = self.validCount() - 1
        for normalized in nSizes:
            a += (pow((normalized - avg), 2))
        return sqrt(a / b)
        