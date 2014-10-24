'''
Created on Oct 21, 2014

@author: Taylor
'''
from __builtin__ import str
import os 

class PythonScript(object):
    

    def __init__(self, fileNameIn=""):
        
        ip_length = len(fileNameIn)
        instance = isinstance(fileNameIn, str)
        p = os.path.abspath("testFiles/" + fileNameIn)
        
        if(instance and ip_length > 3 and fileNameIn.endswith(".py")):
            self.fileName = fileNameIn
        else:
            raise ValueError("PythonScript.__init__:  you didn't provide a valid fileName")
        
        if(os.path.exists(p)):
            self.path = p
        else:
            raise ValueError("PythonScript.__init__:  the file path doesn't actually exist.")
   
    def getFileName(self):
        return self.fileName 
    
    def getFilePath(self):
        return self.path
        