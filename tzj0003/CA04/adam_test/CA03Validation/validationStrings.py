'''
    Validation Suite:  Strings
    Baselined:  29 Sep 2013
    Modified:  10 Oct 2014
    @author:  D. Umphress
        Component("EvilStrings", 1, 13)
        Total LOC = 13
'''

class EvilStrings:

    emptyString1 = ""
    emptyString2 = ''
    emptyString3 = """"""
    emptyString4 = ''''''
    
    oneLineString1 = "abc"
    oneLineString2 = 'abc'
    oneLineString3 = '''"abc'''
    oneLineString4 = "'''"
    
    multiLineString1 = ' abc ' + \
        'abc '
    
    
    def __init__(self, initString):
        self.internalString = initString + '''   '''
        