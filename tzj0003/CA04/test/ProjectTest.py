'''
Created on Nov 4, 2014

@author: Taylor
'''
import unittest
import CA04.prod.Iteration as Iteration
import CA04.prod.Project as Project

class Test(unittest.TestCase):
    
    def test100_010_shouldConstructProject(self):
        project = Project.Project()
        self.assertIsInstance(project, Project.Project)
    
    def test200_010_shouldAddIteration(self):
        project = Project.Project()
        iteration1 = Iteration.Iteration(effort=20, plannedVelocity=4)
        iteration2 = Iteration.Iteration(effort=40, plannedVelocity=9)
        project.add(iteration1)
        self.assertEquals(project.add(iteration2), 2)
    
    def test200_020_addShouldRejectInvalidParameters(self):
        expectedString = "Project.add:  Invalid Parameters."
        project = Project.Project()
        try:
            project.add(69)                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")