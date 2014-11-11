'''
Created on Nov 3, 2014

@author: Taylor
'''

import unittest
import CA04.prod.Iteration as Iteration

class Test(unittest.TestCase):

# Constructor
    def test100_010_shouldConstructIteration(self):
        myIteration = Iteration.Iteration(effort=120, plannedVelocity=3)
        self.assertIsInstance(myIteration, Iteration.Iteration)
   
    def test100_020_shouldRejectInvalidEffort(self):
        expectedString = "Iteration.__init__:  "
        try:
            Iteration.Iteration(effort="poop", plannedVelocity=3)                                               
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
    
    def test100_030_shouldRejectInvalidVelocity(self):
        expectedString = "Iteration.__init__:  "
        try:
            Iteration.Iteration(effort=24, plannedVelocity="55")                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")

# Iteration.getEffort()    
    def test200_010_shouldReturnIterationEffort(self):
        myIteration = Iteration.Iteration(effort=120, plannedVelocity=3)
        self.assertEquals(myIteration.getEffort(), 120)
    
    def test300_010_shouldReturnIterationPlannedVelocity(self):
        myIteration = Iteration.Iteration(effort=120, plannedVelocity=3)
        self.assertEquals(myIteration.getPV(), 3)
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()