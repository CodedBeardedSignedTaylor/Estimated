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
    
    def test300_010_shouldReturnIterationCount(self):
        project = Project.Project()
        project.add(Iteration.Iteration(effort=120, plannedVelocity=12))
        project.add(Iteration.Iteration(effort=100, plannedVelocity=8))
        project.add(Iteration.Iteration(effort=130, plannedVelocity=20))
        iterations = project.getIterationCount()
        self.assertEquals(iterations, 3)
    
    def test400_010_shouldGetRequestedIteration(self):
        project = Project.Project()
        project.add(Iteration.Iteration(effort=120, plannedVelocity=12))
        iteration = project.getIteration(iterationNumber=1)
        self.assertEquals(iteration, project.iterations[0])
    
    def test400_020_shouldRejectInvalidIterationIndex(self):
        expectedString = "Project.getIteration:  you didn't provide an int index"
        project = Project.Project()
        project.add(Iteration.Iteration(effort=120, plannedVelocity=12))
        try:
            project.getIteration(-1)                                               
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
    
    def test500_010_shouldGetProjectEffort(self):
        project = Project.Project()
        project.add(Iteration.Iteration(effort=120, plannedVelocity=12))
        project.add(Iteration.Iteration(effort=100, plannedVelocity=8))
        project.add(Iteration.Iteration(effort=130, plannedVelocity=20))
        self.assertEquals(project.getEffort(), 350)
    
    def test600_010_shouldGetProjectedPV(self):
        project = Project.Project()
        project.add(Iteration.Iteration(effort=120, plannedVelocity=12))
        project.add(Iteration.Iteration(effort=100, plannedVelocity=8))
        project.add(Iteration.Iteration(effort=130, plannedVelocity=20))
        self.assertEquals(project.getPV(), 40)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()