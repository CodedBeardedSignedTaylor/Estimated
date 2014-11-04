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
        iteration = Iteration.Iteration(effort=20, projectedVelocity=4)
        self.assertEquals(project.addIteration(iteration), 1)
    
    def test200_020_addShouldRejectInvalidParameters(self):
        expectedString = "Project.add:  invalid parameters"
        project = Project.Project()
        try:
            project.add(69)                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")