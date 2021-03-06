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
            if(day > 0 and effort > -1):
                # Create day object.
                d = Day.Day(day, effort)
                index = self.checkForDup(day)
                if(index > 0):
                    self.days[index] = d
                else:
                    self.days.append(d)
                self.effort += d.getEffort()
        
                return self.effort
            else:
                raise ValueError("Calendar.add:  num and effort must be greater than 0.")
        else:
            raise ValueError("Calendar.add:  invalid parameters.")
    
    def checkForDup(self, day):
        for d in self.days:
            if(day == d.getNumber()):
                return self.days.index(d)
        return -1
    
    def getLength(self):
        
        highest_day = 0
        
        for d in self.days:
            day_num = d.getNumber()
            if(day_num > highest_day and d.getEffort() > 0):
                highest_day = day_num
        
        return highest_day

    def get(self, day):
        
        # Check to see if the user passed in a valid day.
        if(isinstance(day, int) and day > 0):
            for d in self.days:
                if (d.getNumber() == day):
                    return d.getEffort()
            
            # In the case that our for loop doesn't find the day....
            raise ValueError("Calendar.get:  Could not find requested day.")
        else: 
            raise ValueError("Calendar.get:  invalid parameters.")
    
    def getDay(self, day_num):
        if(isinstance(day_num, int) and day_num > 0):
            for d in self.days:
                if (d.getNumber() == day_num):
                    return d
            
            # In the case that our for loop doesn't find the day....
            raise ValueError("Calendar.get:  Could not find requested day.")
        else: 
            raise ValueError("Calendar.get:  invalid parameters.")
    
    def getEffort(self):
        effort = 0
        for d in self.days:
            effort += d.getEffort()
        
        return effort         
        