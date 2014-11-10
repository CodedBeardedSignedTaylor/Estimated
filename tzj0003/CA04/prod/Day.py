'''
Created on Nov 6, 2014

@author: Taylor
'''

class Day(object):
    '''
    classdocs
    '''


    def __init__(self, number, effort):
        if(number > 0 and effort > 0):
            self.number = number
            self.effort = effort
        else:
            raise ValueError("Day.__init__:  You didn't do something right.")
        
    def getNumber(self):
        return self.number
    
    def getEffort(self):
        return self.effort
    