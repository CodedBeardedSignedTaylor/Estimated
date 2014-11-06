'''
Created on Nov 6, 2014

@author: Taylor
'''
import CA04.prod.Day as Day


class Calendar(object):

    def __init__(self):
        self.days = []
        self.effort = 0
    
    def add(self, day, effort):
        
        if(isinstance(day, int) and isinstance(effort, int)):
            if(day > 0 and effort > 0):
                d = Day.Day(day, effort)
                self.days.append(d)
        
                self.effort += d.getEffort()
        
                return self.effort
            else:
                raise ValueError("Calendar.add:  num and effort must be greater than 0.")
        else:
            raise ValueError("Calendar.add:  invalid parameters.")
            