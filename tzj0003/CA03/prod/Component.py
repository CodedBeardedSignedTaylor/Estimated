'''
Created on Sep 11, 2014

@author: Taylor
'''

class Component(object):

    def __init__(self, name=None, methodCount=None, locCount=None):
        if(isinstance(name, str) == False or name == "" or name == None):
            raise ValueError("Component.__init__:  ")
        if (isinstance(methodCount, str) or methodCount < 0 or methodCount == None):
            raise ValueError("Component.__init__:  ")
        if(isinstance(locCount, str) or locCount < 1 or locCount == None):
            raise ValueError("Component.__init__:  ")
        
        self.name = name
        self.methodCount = methodCount
        self.locCount = locCount
        self.relativeSize = None
    
    def getName(self):
        return self.name
    
    def getMethodCount(self):
        return self.methodCount
    
    def getLocCount(self):
        return self.locCount
    
    def setRelativeSize(self, size="M"):
        size = size.upper()
        if(size == "VS" or size == "S" or size == "M" or size == "L" or size == "VL"):
            self.relativeSize = size
            return self.relativeSize
        elif(isinstance(size, str) == False):
            raise ValueError("Component.setRelativeSize:  ")
        else:
            raise ValueError("Component.setRelativeSize:  ")
        
    def getRelativeSize(self):
        if(self.relativeSize == None):
            raise ValueError("Component.getRelativeSize:  ")
        else:
            return self.relativeSize
    