'''
Created on Nov 3, 2014

@author: Taylor
'''
from __builtin__ import int

class Iteration(object):

    def __init__(self, effort, plannedVelocity):
        
        if(effort > 0 and isinstance(effort, int)):
            self.effort = effort
        else:
            raise ValueError("Iteration.__init__:  Effort needs to be an integer > 0.")
        if(plannedVelocity > 0 and isinstance(plannedVelocity, int)):
            self.plannedVelocity = plannedVelocity
        else:
            raise ValueError("Iteration.__init__:  PV needs to be an integer > 0")
    
    def getEffort(self):
        return self.effort
    
    def getPV(self):
        return self.plannedVelocity
      
        