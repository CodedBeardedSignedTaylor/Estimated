'''
Created on Nov 4, 2014

@author: Taylor
'''
import CA04.prod.Iteration as Iteration

class Project(object):

    def __init__(self):
        self.iterations = []
    
    def add(self, iteration):
        if(isinstance(iteration, Iteration.Iteration) == False):
            raise ValueError("Project.add:  Invalid Parameters.")
        else:
            self.iterations.append(iteration)
            index = len(self.iterations)
            return index