'''
Created on Sep 11, 2014

@author: Taylor
'''

from lib2to3.fixer_util import String

class Component(object):

    def __init__(self, name, methodCount, locCount):
        if(isinstance(name, str)):
            self.name = name
        else:
            raise(ValueError)
        if(isinstance(methodCount, str) or methodCount < 0):
            raise(ValueError)
        else:
            self.methodCount = methodCount
        if(isinstance(locCount, str) or locCount < 1):
            raise(ValueError)
        else:
            self.locCount = locCount
    
    def getName(self):
        return self.name
    
    def getMethodCount(self):
        return self.methodCount
    
    def getLocCount(self):
        return self.locCount
    