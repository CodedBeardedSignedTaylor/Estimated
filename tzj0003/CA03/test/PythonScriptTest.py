'''
Created on Oct 21, 2014

@author: Taylor
'''
import unittest
# import CA03.prod.Component as Component
# import CA03.prod.Repository as Repository
import CA03.prod.PythonScript as PythonScript
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
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()