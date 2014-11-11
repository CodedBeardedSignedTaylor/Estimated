'''
Created on Nov 4, 2014

@author: Taylor
'''
import CA04.prod.Iteration as Iteration
from __builtin__ import int

class Project(object):

    def __init__(self):
        self.iterations = []
    
    def add(self, iteration=None):
        if(isinstance(iteration, Iteration.Iteration) == False or iteration == None):
            raise ValueError("Project.add:  Invalid Parameters.")
        else:
            self.iterations.append(iteration)
            index = len(self.iterations)
            return index
        
    
    def getIterationCount(self):
        return len(self.iterations)
    
    def getIteration(self, iterationNumber):
        if(isinstance(iterationNumber, int) == True and iterationNumber > 0):
            iteration = self.iterations[iterationNumber - 1]
            return iteration
        else:
            raise ValueError("Project.getIteration:  you didn't provide an int index")
    
    def getEffort(self):
        effort = 0
        iterations = self.iterations
        for itr in iterations:
            effort += itr.getEffort()
        
        return effort
    
    def getPV(self):
        pv = 0
        iterations = self.iterations
        for itr in iterations:
            pv += itr.getPV()
        
        return pv