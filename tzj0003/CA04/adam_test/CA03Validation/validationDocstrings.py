'''
    Validation Suite:  Docstrings
    Baselined:  29 Sep 2013
    Modified:  10 Oct 2014
    @author:  D. Umphress
        Component("docStringFunction1",1,2)
	    Component("docStringFunction2",1,2)
	    Component("docStringFunction3",1,2)
	    Component("DocStringClassA",4,9)
	    Total LOC = 15
	    
def nonfunction():
    pass
'''

def docStringFunction1():
    """
        multi-line docstring with 
        symmetrically-formatted  delimiters
    """
    pass

def docStringFunction2():
    """  one-line docstring """
    pass

def docStringFunction3():
    """
        multi-line docstring with asymmetrically-
        formatted delimiters """
    pass


class DocStringClassA():
    '''
        multi-line class docstring with 
        symmetrically-formatted  delimiters
    '''

    def __init__(self):
        "  one-line method docstring "
        pass

    def docStringMethod1(self):
        '  one-line method docstring '
        pass

    def docStringMethod2(self):
        '''  one-line method docstring '''
        pass

    def docStringMethod3(self):
        '''  multi-line method docstring with
        
        blank line'''
        pass