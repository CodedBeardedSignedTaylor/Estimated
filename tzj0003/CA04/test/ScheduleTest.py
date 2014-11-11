'''
Created on Nov 10, 2014

@author: Taylor
'''
import unittest
import CA04.prod.Iteration as Iteration
import CA04.prod.Project as Project
import CA04.prod.Schedule as Schedule 
import CA04.prod.Calendar as Calendar

class Test(unittest.TestCase):
    
    def test100_010_shouldConstructSchedule(self):
        cal = Calendar.Calendar()
        proj = Project.Project()
        s = Schedule.Schedule(proj, cal)
        self.assertIsInstance(s, Schedule.Schedule)
    
    def test100_020_shouldRejectInvalidProjectParam(self):
        expectedString = "Schedule.__init__:  incorrect parameter types."
        cal = Calendar.Calendar()
        try:
            Schedule.Schedule("hello", cal)                                               
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
    
    def test100_030_shouldRejectInvalidCalParam(self):
        expectedString = "Schedule.__init__:  incorrect parameter types."
        proj = Project.Project()
        try:
            Schedule.Schedule(proj, 22)                                               
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
    
    def test200_010_shouldGetLastDay(self):
        # Create calendar and add days.
        cal = Calendar.Calendar()
        cal.add(day=1, effort=10)
        cal.add(day=2, effort=0)
        cal.add(day=3, effort=30)
        cal.add(day=4, effort=30)
        cal.add(day=5, effort=60)
        cal.add(day=6, effort=90)
        # Create Project and add iterations.
        proj = Project.Project()
        proj.add(Iteration.Iteration(effort=30, plannedVelocity=1))
        proj.add(Iteration.Iteration(effort=60, plannedVelocity=3))
        s = Schedule.Schedule(proj, cal)
        self.assertEquals(s.getLastDay(), 5)
    
    def test300_010_shouldGetBurndownForSpecifiedDay(self):
        # Create calendar and add days.
        cal = Calendar.Calendar()
        cal.add(day=1, effort=10)
        cal.add(day=2, effort=0)
        cal.add(day=3, effort=30)
        cal.add(day=4, effort=30)
        cal.add(day=5, effort=60)
        cal.add(day=6, effort=90)
        # Create Project and add iterations.
        proj = Project.Project()
        proj.add(Iteration.Iteration(effort=30, plannedVelocity=1))
        proj.add(Iteration.Iteration(effort=60, plannedVelocity=3))
        s = Schedule.Schedule(proj, cal)
        self.assertEquals(s.getBurnDown(day=3), 50)
    
    def test300_020_shouldRejectInvalidDay(self):
        expectedString = "Schedule.getBurnDown:  requested day not in range."
        # Create calendar and add days.
        cal = Calendar.Calendar()
        cal.add(day=1, effort=10)
        cal.add(day=2, effort=0)
        cal.add(day=3, effort=30)
        cal.add(day=4, effort=30)
        cal.add(day=5, effort=60)
        cal.add(day=6, effort=90)
        # Create Project and add iterations.
        proj = Project.Project()
        proj.add(Iteration.Iteration(effort=30, plannedVelocity=1))
        proj.add(Iteration.Iteration(effort=60, plannedVelocity=3))
        s = Schedule.Schedule(proj, cal)
        try:
            s.getBurnDown(400)                                             
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
    
    def test400_010_shouldReturnPV(self):
        # Create calendar and add days.
        cal = Calendar.Calendar()
        cal.add(day=1, effort=10)
        cal.add(day=2, effort=0)
        cal.add(day=3, effort=30)
        cal.add(day=4, effort=30)
        cal.add(day=5, effort=60)
        cal.add(day=6, effort=90)
        # Create Project and add iterations.
        proj = Project.Project()
        proj.add(Iteration.Iteration(effort=30, plannedVelocity=1))
        proj.add(Iteration.Iteration(effort=60, plannedVelocity=3))
        s = Schedule.Schedule(proj, cal)
        
        self.assertEquals(s.getPV(day=3), 3)
    
    def test400_020_shouldRejectInvalidDay(self):
        expectedString = "Schedule.getPV:  requested day not in range."
        # Create calendar and add days.
        cal = Calendar.Calendar()
        cal.add(day=1, effort=10)
        cal.add(day=2, effort=0)
        cal.add(day=3, effort=30)
        cal.add(day=4, effort=30)
        cal.add(day=5, effort=60)
        cal.add(day=6, effort=90)
        # Create Project and add iterations.
        proj = Project.Project()
        proj.add(Iteration.Iteration(effort=30, plannedVelocity=1))
        proj.add(Iteration.Iteration(effort=60, plannedVelocity=3))
        s = Schedule.Schedule(proj, cal)
        try:
            s.getPV(400)                                             
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()