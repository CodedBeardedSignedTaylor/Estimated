'''
    Validation Suite:  Classes
    Baselined:  29 Sep 2013
    Modified:  10 Oct 2014
    @author:  D. Umphress
          Component("ClassA",2,5)
          Component("ClassB",1,3)
          Component("ClassC",0,2)
          Total LOC = 12
'''

import sys

class ClassA():
    def __init__(self):
        pass

    def methodA(self, parm1=""):
        pass


class ClassB(ClassA):
    def methodB(self):
        pass


class ClassC(ClassB):
        pass


pass