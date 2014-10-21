'''
Created on Oct 21, 2014

@author: Taylor
'''
import unittest
# import CA03.prod.Component as Component
# import CA03.prod.Repository as Repository
import CA03.prod.PythonScript as PythonScript


class Test(unittest.TestCase):

    def test100_010_shouldConstructPythonScript(self):
        self.assertIsInstance(PythonScript.PythonScript(file="text.txt"), PythonScript.PythonScript)
    
    def test100_020_shouldRejectFileNamesLessThan4(self):
        expectedString = "PythonScript.__init__:"
        try:
            PythonScript.PythonScript(".py")                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()