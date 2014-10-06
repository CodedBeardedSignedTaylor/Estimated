'''
Created on Sep 11, 2014

@author: Taylor
'''

class Component(object):

    def __init__(self, name=None, methodCount=None, locCount=None):
        if(isinstance(name, str) == False or name == "" or name == None):
            raise ValueError("Component.__init__:")
        if (isinstance(methodCount, str) or methodCount < 0 or methodCount == None):
            raise ValueError("Component.__init__:")
        if(isinstance(locCount, str) or locCount < 1 or locCount == None):
            raise ValueError("Component.__init__:")
        
        self.name = name
        self.methodCount = methodCount
        self.locCount = locCount
    
    def getName(self):
        return self.name
    
    def getMethodCount(self):
        return self.methodCount
    
    def getLocCount(self):
        return self.locCount
    