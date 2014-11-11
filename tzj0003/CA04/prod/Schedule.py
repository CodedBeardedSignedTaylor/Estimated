'''
Created on Nov 10, 2014

@author: Taylor
'''

import CA04.prod.Calendar as Calendar
import CA04.prod.Project as Project

class Schedule(object):

    def __init__(self, project, calendar):
        
        if(isinstance(project, Project.Project) and isinstance(calendar, Calendar.Calendar)):
            self.project = project
            self.calendar = calendar
        else:
            raise ValueError("Schedule.__init__:  incorrect parameter types.")
    
    def getLastDay(self):
        remaining_effort = self.project.getEffort()
        i = 1
        cal = self.calendar
        
        while i < cal.getLength():
            d = cal.getDay(i)
            day_effort = d.getEffort()
            remaining_effort -= day_effort
            if(remaining_effort < 1):
                return d.getNumber()
            i += 1
    
    def getBurnDown(self, day):
        
        if(isinstance(day, int) == False):
            raise ValueError("Schedule.getBurnDown:  incorrect day parameter.")
        
        if(day > self.calendar.getLength()):
            raise ValueError("Schedule.getBurnDown:  requested day not in range.")
        
        remaining_effort = self.project.getEffort()
        
        if(day < 1):
            return remaining_effort
        else:
        
            i = 1
            cal = self.calendar
        
            while i < day + 1:
                d = cal.getDay(i)
                day_effort = d.getEffort()
                remaining_effort -= day_effort
                i += 1
        
            return remaining_effort
    
    def getPV(self, day):
        if(isinstance(day, int) == False):
            raise ValueError("Schedule.getPV:  incorrect day parameter.")
        
        if(day > self.calendar.getLength()):
            raise ValueError("Schedule.getPV:  requested day not in range.")
        
        remaining_pv = self.project.getPV()
        
        i = 1
        j = 1
        finished = True
        cal = self.calendar
        
        while i < day + 1:
            
            if(finished == True):
                iteration = self.project.getIteration(j)
                iteration_effort = iteration.getEffort()
                iteration_pv = iteration.getPV()
            else:
                d = cal.getDay(i)
                iteration_effort -= d.getEffort()
            
            if(iteration_effort < 1):
                j += 1
                remaining_pv -= iteration_pv
                finished = True
                i += 1
            else:
                finished = False
                i += 1
        
        return remaining_pv
    