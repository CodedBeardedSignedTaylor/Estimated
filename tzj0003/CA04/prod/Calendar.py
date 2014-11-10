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
                # Create day object and add it to the list.
                d = Day.Day(day, effort)
                self.days.append(d)
        
                self.effort += d.getEffort()
        
                return self.effort
            else:
                raise ValueError("Calendar.add:  num and effort must be greater than 0.")
        else:
            raise ValueError("Calendar.add:  invalid parameters.")
    
    def getLength(self):
        
        highest_day = 0
        
        for d in self.days:
            day_num = d.getNumber()
            if(day_num > highest_day):
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