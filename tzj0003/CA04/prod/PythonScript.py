'''
Created on Oct 21, 2014

@author: Taylor
'''
from __builtin__ import str
import os 
from CA04.prod.Component import Component

class PythonScript(object):
    
    def __init__(self, fileName=""):
        
        if(isinstance(fileName, str) == False):
            raise ValueError("PythonScript.__init__:  ")
        
        if(len(fileName) > 3 and fileName.endswith(".py")):
            self.fileName = fileName
            self.path = self.checkPath(fileName)
        else:
            raise ValueError("PythonScript.__init__:  you didn't provide a valid fileName")
        
    def checkPath(self, fileName):
        p = os.path.abspath(fileName)
        if(os.path.isfile(p)):
            return p
        else:
            raise ValueError("PythonScript.__init__:  the file path doesn't actually exist.")
   
    def getFileName(self):
        return self.fileName 
    
    def getFilePath(self):
        return self.path
    
    def countLoc(self):
        with open(self.getFilePath()) as myfile:
            count = sum(1 for line in myfile if line.rstrip('\n'))
        return count
    
    def extractName(self, line):
        full_ln = line.split()
        piece = full_ln[1].split('(')
        name = piece[0]
        return name
    
    def analyzeLine(self, line, isFunction):
        
        
        if(line.startswith("class")):
            return "class"
        elif(line.startswith("def")):
            return "function"
        elif(line.startswith("    def")):
            return "method"
        elif(line.startswith("        ")):
            line = line.strip()
            
            if(line == ""):
                return "whiteSpace"
            else:
                return "basicLine"
        elif(line.startswith("#")):
            return "comment"
        
        if(isFunction):
            line = line.strip()
            if(line == ""):
                return "whitespace"
            else:
                return "basicLine"
    
    def extractDesign(self):
        classDesigns = []
        funcDesigns = []
        started = False
        isClass = False
        isFunction = False
        
        locCount = 0
        ws_count = 0
        name = None
        methodCount = 0
    
        myFile = open(self.getFilePath(), 'r')
        for line in myFile:
            
            which = self.analyzeLine(line, isFunction)
            
            if(which == "class"):
                if(started == True):
                    locCount = locCount - ws_count
                    comp = Component(name, methodCount, locCount)
                    
                    if(isClass):
                        classDesigns.append(comp)
                    elif(isFunction):
                        funcDesigns.append(comp)
                    
                name = self.extractName(line)
                methodCount = 0
                locCount = 1
                ws_count = 0
                isClass = True
                isFunction = False
                started = True
                continue
                    
            elif(which == "function"):
                if(started == True):
                    locCount -= ws_count
                    comp = Component(name, methodCount, locCount)
                    
                    if(isClass):
                        classDesigns.append(comp)
                    else:
                        funcDesigns.append(comp)
            
                name = self.extractName(line)
                methodCount = 1
                locCount = 1
                ws_count = 0
                isFunction = True
                isClass = False
                started = True
                continue
            
            elif(which == "basicLine" or which == "comment"):
                locCount += 1
            
            elif(which == "whiteSpace"):
                ws_count += 1
            
            elif(which == "method"):
                methodCount = methodCount + 1
                locCount += 1
        else:
            locCount -= ws_count
            comp = Component(name, methodCount, locCount)
            if(isClass):
                classDesigns.append(comp)
            elif(isFunction):
                funcDesigns.append(comp)
            myFile.close()             
            return [classDesigns, funcDesigns]             
        