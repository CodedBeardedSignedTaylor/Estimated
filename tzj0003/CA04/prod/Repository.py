'''
Created on Sep 14, 2014

@author: Taylor
'''
from CA03.prod.Component import Component
from math import sqrt, ceil, exp, log
from __builtin__ import str, int

class Repository(object):

    def __init__(self, capacity=100):
        if(isinstance(capacity, int) and capacity > 0):
            self.capacity = capacity
            self.components = []
            self.componentCount = 0
        else:
            raise ValueError("Repository.__init__:  invalid parameters")
    
    def addComponent(self, component=None):
        if (isinstance(component, Component)):
            if(self.checkForDup(component.getName()) == True):
                raise ValueError("Repository.addComponent:  ")
            if(len(self.components) == self.capacity):
                self.components.pop(0)
            self.components.append(component)
            self.componentCount = len(self.components)
            return len(self.components)
        else:
            raise ValueError("Repository.addComponent:  you didn't provide a Component.") 
    
    def checkForDup(self, name):
        for comp in self.components:
            if(comp.getName() == name):
                return True
        return False
    
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
            raise ValueError ("Repository.determineRelativeSizes:  ")
        nSizes = self.calculateNormalizedSizes()
        avg = self.calculateAverage(nSizes)
        std = self.calculateStdDeviation(avg, nSizes)
        
        verySmall = int(ceil(exp(avg - (2 * std))))
        small = int(ceil(exp(avg - std)))
        medium = int(ceil(exp(avg)))
        large = int(ceil(exp(avg + std)))
        veryLarge = int(ceil(exp(avg + (2 * std))))
        return [verySmall, small, medium, large, veryLarge]
    
    def getRelativeSize(self, component=None):
        if (self.validCount() < 2 or component == None):
            raise ValueError("Repository.getRelativeSize:  ")
        if(component.getMethodCount() == 0):
            raise ValueError("Repository.getRelativeSize:  ")
        
        nSizes = self.calculateNormalizedSizes()
        avg = self.calculateAverage(nSizes)
        std = self.calculateStdDeviation(avg, nSizes)
        
        inputSize = (component.getLocCount() / component.getMethodCount())
        
        verySmall = int(ceil(exp(avg - (2 * std))))
        small = int(ceil(exp(avg - std)))
        medium = int(ceil(exp(avg)))
        large = int(ceil(exp(avg + std)))
        veryLarge =  int(ceil(exp(avg + (2 * std))))
        
        if(inputSize >= veryLarge):
            return "VL"
        elif(inputSize >= large):
            return "L"
        elif(inputSize >= medium):
            return "M"
        elif(inputSize >= small):
            return "S"
        elif(inputSize <= verySmall):
            return "VS" 
        else:
            raise ValueError ("Repository.getRelativeSize:  ")
        
    def calculateNormalizedSizes(self):
        normalizedSizes = []
        for comp in self.components:
            if(comp.getMethodCount() > 0):
                result = self.normalize(comp)
                normalizedSizes.append(result)   
        return normalizedSizes
    
    def normalize(self, component):
        loc = float(component.getLocCount())
        meth = float(component.getMethodCount())
        a = float(loc / meth)
        normalizedSize = abs(log(a))
        return normalizedSize
        
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
    
    def estimateByRelativeSize(self, name=None, methodCount=None, size=None):
        inputSize = size
        if(isinstance(name, str) == False or isinstance(methodCount, int) == False):
            raise ValueError("Repository.estimateByRelativeSize:  nonvalid type parameters")
        if(name == None or methodCount == None or name == ""):
            raise ValueError("Repository.estimateByRelativeSize:  missing parameter")
        if(self.checkForDup(name) == True or self.validCount() < 2 or methodCount <= 0):
            raise ValueError("Repository.estimateByRelativeSize:  invalid parameter(s)")
        else:
            if(inputSize == None):
                inputSize = "M"
            inputSize = inputSize.upper()
            dSizes = self.determineRelativeSizes()
            
            for size in dSizes:
                if(size == 0):
                    raise ValueError("Repository.estimateRelativeSize:  ")
            
            if(inputSize == "VS"):
                loc = methodCount * dSizes[0]
            elif(inputSize == "S"):
                loc = methodCount * dSizes[1]
            elif(inputSize == "M"):
                loc = methodCount * dSizes[2]
            elif(inputSize == "L"):
                loc = methodCount * dSizes[3]
            elif(inputSize == "VL"):
                loc = methodCount * dSizes[4]
            else:
                raise ValueError("Repository.estimateByRelativeSize:  ")
            
            comp = Component(name, methodCount, loc)
            return comp    