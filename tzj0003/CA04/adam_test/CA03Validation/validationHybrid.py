'''
    Validation Suite:  Hybrid 
    Baselined:  29 Sep 2013
    Modified:  10 Oct 2014
    @author:  D. Umphress
        Component("HybridClassA",3,7)
        Component("HybridClassB",0,2)
        Component("hybridFunctionA",1,2)
        Component("hybridFunctionB",1,2)
        Component("hybridFunctionC",1,2)
        Total LOC = 21
'''

import sys
import unittest

class HybridClassA():
    def __init__(self):
        pass

    def methodA(self, parm1=""):
        pass

    def methodB(self, parm1, parm2):
        pass


class HybridClassB():
    pass


def hybridFunctionA(parm1=""):
    pass

def hybridFunctionB():
    pass

def hybridFunctionC(*parms):
    pass

# The following code is outside of a component
if __name__ == "__main__":
    pass
pass
pass