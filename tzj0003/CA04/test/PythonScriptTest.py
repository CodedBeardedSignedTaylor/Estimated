'''
Created on Oct 21, 2014

@author: Taylor
'''
import unittest
import CA04.prod.Component as Component
# import CA03.prod.Repository as Repository
import CA04.prod.PythonScript as PythonScript
import os


class Test(unittest.TestCase):

# Constructor Tests
    # Happy Path
    def test100_010_shouldConstructPythonScript(self):
        self.assertIsInstance(PythonScript.PythonScript(fileNameIn="test.py"), PythonScript.PythonScript)
    
    # Sad Path
    def test100_020_shouldRejectFileNamesLessThan4(self):
        expectedString = "PythonScript.__init__:  you didn't provide a valid fileName"
        try:
            PythonScript.PythonScript(".py")                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
            
    def test100_030_fileShouldBePythonFile(self):
        expectedString = "PythonScript.__init__:  you didn't provide a valid fileName"
        try:
            PythonScript.PythonScript("thisIsntReal.px")                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
            
    def test100_040_shouldHaveValidPath(self):
        expectedString = "PythonScript.__init__:  "
        try:
            PythonScript.PythonScript("thisIsntReal.py")                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")

# getFileName()

    def test200_010_shouldReturnFileName(self):
        script = PythonScript.PythonScript(fileNameIn="test.py")
        fileName = script.getFileName()
        self.assertEquals(fileName, "test.py")

# getFilePath()

    def test300_010_shouldReturnFilePath(self):
        script = PythonScript.PythonScript(fileNameIn="test.py")
        p = os.path.abspath("testFiles/" + script.getFileName())
        path = script.getFilePath()
        self.assertEquals(path, p)
        
# countLoc()
    def test400_010_shouldReturnLocCount(self):
        script = PythonScript.PythonScript(fileNameIn="test.py")
        f = open(script.getFilePath())
        count = 0
        for line in f:
            if(line.startswith("         ") == False):
                count = count + 1
        self.assertEquals(count, script.countLoc())

# extractDesign()
    
    def test500_010_componentsShouldHaveProperNames(self):
        script = PythonScript.PythonScript(fileNameIn="test.py")
        design = script.extractDesign()
        a = Component.Component("TestClass", 3, 10)
        b = Component.Component("TestClass2", 3, 10)
        c = Component.Component("function", 1, 3)
        classes = [a, b]
        functions = [c]
        components = [classes, functions]
        
        for i in range(0, len(classes) - 1):
            self.assertEquals(design[0][i].name, components[0][i].name)

        for j in range(0, len(functions) - 1):
            self.assertEquals(design[1][j].name, components[1][j].name)
    
    def test500_020_componentsShouldHaveProperMethodCounts(self):
        script = PythonScript.PythonScript(fileNameIn="test.py")
        design = script.extractDesign()
        a = Component.Component("TestClass", 3, 10)
        b = Component.Component("TestClass2", 3, 10)
        c = Component.Component("function", 1, 3)
        classes = [a, b]
        functions = [c]
        components = [classes, functions]
        
        for i in range(0, len(classes) - 1):
            self.assertEquals(design[0][i].methodCount, components[0][i].methodCount)

        for j in range(0, len(functions) - 1):
            self.assertEquals(design[1][j].methodCount, components[1][j].methodCount)

    def test500_030_componentsShouldHaveProperLocCounts(self):
        script = PythonScript.PythonScript(fileNameIn="test.py")
        design = script.extractDesign()
        a = Component.Component("TestClass", 3, 10)
        b = Component.Component("TestClass2", 3, 10)
        c = Component.Component("function", 1, 2)
        classes = [a, b]
        functions = [c]
        components = [classes, functions]
        
        for i in range(0, len(classes) - 1):
            self.assertEquals(design[0][i].locCount, components[0][i].locCount)

        for j in range(0, len(functions) - 1):
            self.assertEquals(design[1][j].locCount, components[1][j].locCount)
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()