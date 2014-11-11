import unittest
# import CA04.prod.Project as Project
# import CA04.prod.Iteration as Iteration
import CA04.prod.Calendar as Calendar

class TestComponent(unittest.TestCase):
    
    def test100_010_shouldConstructCalendar(self):
        cal = Calendar.Calendar()
        self.assertIsInstance(cal, Calendar.Calendar)
    
    def test200_010_shouldAddDayToCalendar(self):
        cal = Calendar.Calendar()
        cal.add(day=1, effort=25)
        a = cal.add(day=2, effort=30)
        self.assertEquals(a, 55)
    
    def test200_020_shouldRejectInvalidDay(self):
        expectedString = "Calendar.add:  invalid parameters."
        cal = Calendar.Calendar()
        try:
            cal.add(day="today", effort=20)
            self.fail("exception was not raised")
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
    
    def test200_030_shouldRejectInvalidEffort(self):
        expectedString = "Calendar.add:  invalid parameters."
        cal = Calendar.Calendar()
        try:
            cal.add(day=3, effort="hard")                                               
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
    
    def test200_040_shouldOverwriteDuplicates(self):
        cal = Calendar.Calendar()
        cal.add(day=1, effort=25)
        cal.add(day=2, effort=30)
        cal.add(day=1, effort=25)
        self.assertEquals(cal.getLength(), 2)
    
    def test300_010_shouldReturnCalendarLength(self):
        cal = Calendar.Calendar()
        cal.add(day=1, effort=25)
        cal.add(day=12, effort=30)
        cal.add(day=15, effort=2)
        self.assertEquals(cal.getLength(), 15)
    
    def test400_010_shouldReturnRequestedDay(self):
        cal = Calendar.Calendar()
        cal.add(day=1, effort=25)
        cal.add(day=30, effort=30)
        self.assertEquals(cal.get(30), 30)
    
    def test400_020_shouldRejectInvalidDayParameters(self):
        expectedString = "Calendar.get:  invalid parameters."
        cal = Calendar.Calendar()
        cal.add(day=1, effort=25)
        cal.add(day=2, effort=30)
        try:
            cal.get(-1)                                               
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()