'''
Created on Sep 9, 2014

@author: Taylor
'''

import unittest

import CA03.prod.Repository as Repository
import CA03.prod.Component as Component
#import CA01.student.Repository as Repository
#import CA01.student.Component as Component

class TestRepository(unittest.TestCase):

# Constructor
    #100_0xx ... happy 
    def test100_010_ShouldConstructRepositoryExplicitCapacity(self):
        self.assertIsInstance(Repository.Repository(capacity=100), Repository.Repository)
        
    def test100_020_ShouldConstructRepositoryDefaultCapacity(self):
        self.assertIsInstance(Repository.Repository(), Repository.Repository)
        
    #100_9xx ... sad path
    def test100_910_ShouldRaiseExceptionOnNonIntCapacity(self):
        expectedString = "Repository.__init__:"
        try:
            myRepository = Repository.Repository("a")                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 
    
    def test100_920_ShouldRaiseExceptionOnInvalidCapacity(self):
        expectedString = "Repository.__init__:"
        try:
            myRepository = Repository.Repository(capacity=0)                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")     

    
# addComponent
    #200_0xx ... happy path
    def test200_010_shouldAddComponent(self):
        maxCapacity = 2
        theRepository = Repository.Repository(maxCapacity)
        for i in range(maxCapacity):
            self.assertEquals(i+1, theRepository.addComponent(Component.Component("C"+str(i), i+1, i+1)))
            
    def test200_020_shouldAddComponentPastCapacity(self):
        maxCapacity = 2
        theRepository = Repository.Repository(maxCapacity)
        for i in range(maxCapacity):
            theRepository.addComponent(Component.Component("C"+str(i), i+1, i+1))
            
        self.assertEquals(maxCapacity, theRepository.addComponent(Component.Component("overflow", 1, 10)))
        
    def test200_020_shouldDeleteOldestPastCapacity(self):
        maxCapacity = 2
        theRepository = Repository.Repository(maxCapacity)
        # Add maxCapacity+1 components
        # Ensure the first one has a zero method count, all others have non-zero method count
        # We infer that the first component -- the only component with a non-zero method count -- has
        # been deleted if validCount() == 2
        for i in range(maxCapacity+1):
            theRepository.addComponent(Component.Component("C"+str(i), i, i+1))
        self.assertEquals(2, theRepository.validCount())
        
    def test200_910_shouldRaiseExceptionIfComponentMissing(self):
        #AMBexpectedString = "Repository.addComponent:  "
        expectedString = "Repository.addComponent:"
        theRepository = Repository.Repository()
        try:                                             
            theRepository.addComponent()
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
    
    def test200_030_shouldDeleteDuplicateNames(self):
        #AMBexpectedString = "Repository.addComponent:  "
        expectedString = "Repository.addComponent:"
        theRepository = Repository.Repository()
        firstComp = Component.Component("This", 4, 20)
        dupComp = Component.Component("This", 5, 40)
        try:                                             
            theRepository.addComponent(firstComp)
            theRepository.addComponent(dupComp)
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
         
# count
    #300_0xx ... happy path
    def test300_010_shouldReturnInt(self):
        maxCapacity = 10
        theRepository = Repository.Repository(maxCapacity)
        for i in range(maxCapacity):
            theRepository.addComponent(Component.Component("C"+str(i), i+1, i+1))
        self.assertIsInstance(theRepository.count(), int)
            
        self.assertEquals(maxCapacity, theRepository.addComponent(Component.Component("overflow", 1, 10)))    
    def test300_020_shouldReturnCount(self):
        maxCapacity = 10
        theRepository = Repository.Repository(maxCapacity)
        for i in range(maxCapacity):
            theRepository.addComponent(Component.Component("C"+str(i), i+1, i+1))
            self.assertEqual(i+1, theRepository.count())
        self.assertEquals(maxCapacity, theRepository.addComponent(Component.Component("overflow", 1, 10)))
        
        
# validCount
    #400_0xx ... happy path
    def test400_010_shouldReturnInt(self):
        maxCapacity = 10
        theRepository = Repository.Repository(maxCapacity)
        for i in range(maxCapacity):
            theRepository.addComponent(Component.Component("C"+str(i), i+1, i+1))
        self.assertIsInstance(theRepository.validCount(), int)  
         
    def test500_010_shouldReturnValidCount(self):
        maxCapacity = 10
        theRepository = Repository.Repository(maxCapacity)
        for i in range(maxCapacity):
            theRepository.addComponent(Component.Component("C"+str(i), 0, i+1))
            self.assertEqual(0, theRepository.validCount())
        
# deteremineRelativeSize
    #600_0xx . . . happy path
    def test600_010_shouldReturnIntList(self):
        maxCapacity = 10
        theRepository = Repository.Repository(maxCapacity)
        methodCounts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        locCounts = [42, 19, 58, 60, 70, 82, 57, 89, 80, 128]
        for i in range(maxCapacity):
            theRepository.addComponent(Component.Component("C"+str(i), methodCounts[i], locCounts[i]))
        listOfSizes = theRepository.determineRelativeSizes()
        self.assertIsInstance(listOfSizes, list)
        for size in listOfSizes:
            self.assertIsInstance(size, int)
        
    def test600_020_shouldReturnSizeList(self):
        # test set:
        #name methods LOC   ln(loc/methods)
        #C0    0    42    NA
        #C1    1    19    2.944438979
        #C2    2    58    3.36729583
        #C3    3    60    2.995732274
        #C4    4    70    2.862200881
        #C5    5    82    2.797281335
        #C6    6    57    2.251291799
        #C7    7    89    2.542726221
        #C8    8    80    2.302585093
        #C9    9    128    2.654805687
        #          avg = 2.746484233
        #          stdev = 0.352645834
        #  This yields [8, 11, 16, 23, 32]
        maxCapacity = 10
        theRepository = Repository.Repository(maxCapacity)
        methodCounts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        locCounts = [42, 19, 58, 60, 70, 82, 57, 89, 80, 128]
        for i in range(maxCapacity):
            theRepository.addComponent(Component.Component("C"+str(i), methodCounts[i], locCounts[i]))
        self.assertListEqual([8, 11, 16, 23, 32], theRepository.determineRelativeSizes())        
        
    def test600_030_shouldReturnSizeList(self):
        # test set:
        #name methods LOC   ln(loc/methods)
        #C0    0    42    NA
        #C1    1    19    2.944438979
        #C2    2    58    3.36729583
        #C3    3    60    2.995732274
        #C4    4    70    2.862200881
        #C5    5    82    2.797281335
        #C6    6    57    2.251291799
        #C7    7    89    2.542726221
        #C8    8    80    2.302585093
        #C9    9    128    2.654805687
        #          avg = 2.746484233
        #          stdev = 0.352645834
        #  This yields [8, 11, 16, 23, 32]
        maxCapacity = 4
        theRepository = Repository.Repository(maxCapacity)
        methodCounts = [1, 4, 7, 5]
        locCounts = [76, 116, 113, 103]
        for i in range(maxCapacity):
            theRepository.addComponent(Component.Component("C"+str(i), methodCounts[i], locCounts[i]))
        self.assertListEqual([8, 15, 30, 58, 115], theRepository.determineRelativeSizes())        
        
    #600_9xx . . . sad path
    def test600_910_shouldRaiseExceptionOnSmallCapacity(self):  
        expectedString = "Repository.determineRelativeSizes:" 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        theRepository.addComponent(Component.Component("LoneComponent", 1, 10))
        try:
            theRepository.determineRelativeSizes()                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 
            
    def test600_920_shouldRaiseExceptionOnTooFewValidComponents(self):  
        expectedString = "Repository.determineRelativeSizes:" 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        theRepository.addComponent(Component.Component("NonZero", 1, 10))
        theRepository.addComponent(Component.Component("Zero", 0, 10))
        try:
            theRepository.determineRelativeSizes()                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")

#getRelativeSize
    def test700_010_shouldReturnCorrectSize(self):
        repo = Repository.Repository()
        a = Component.Component(name="Component01", methodCount=1, locCount=76)
        b = Component.Component(name="Component02", methodCount=4, locCount=116)
        c = Component.Component(name="Component03", methodCount=7, locCount=113)
        d = Component.Component(name="Component04", methodCount=5, locCount=103)
        e = Component.Component(name="Component05", methodCount=0, locCount=10)
        repo.addComponent(a)
        repo.addComponent(b)
        repo.addComponent(c)
        repo.addComponent(d)
        repo.addComponent(e)
        self.assertEquals("L", repo.getRelativeSize(a))
        
    def test700_020_noComponentShouldThrowException(self):
        expectedString = "Repository.getRelativeSize:" 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        try:
            theRepository.getRelativeSize()                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
            
    def test700_030_tooLittleDataShouldThrowException(self):
        expectedString = "Repository.getRelativeSize:" 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        c = Component.Component("NonZero", 1, 10)
        theRepository.addComponent(c)
        try:
            theRepository.getRelativeSize(c)                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")

# estimateRelativeSize
    def test800_010_estimateRelativeSize(self):
        repo = Repository.Repository()
        a = Component.Component(name="Component01", methodCount=1, locCount=76)
        b = Component.Component(name="Component02", methodCount=4, locCount=116)
        c = Component.Component(name="Component03", methodCount=7, locCount=113)
        d = Component.Component(name="Component04", methodCount=5, locCount=103)
        e = Component.Component(name="Component05", methodCount=0, locCount=10)
        
        repo.addComponent(a)
        repo.addComponent(b)
        repo.addComponent(c)
        repo.addComponent(d)
        repo.addComponent(e)
        
        result = repo.estimateRelativeSize("Comp", 5, "S")
        self.assertEquals(75, result.getLocCount())
    
    def test800_020_noNameShouldThrowError(self):
        expectedString = "Repository.estimateRelativeSize:" 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        try:
            theRepository.estimateRelativeSize(methodCount=2, inputSize="S")                                        
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")

    def test800_030_noMethodsInComponentShouldThrowException(self):
        expectedString = "Repository.estimateRelativeSize:" 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        try:
            theRepository.estimateRelativeSize(name="NonZero", methodCount=0, inputSize="M")                                       
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
    
    def test800_040_shouldRaiseValueErrorOnDuplicateComponent(self):
        expectedString = "Repository.estimateRelativeSize:" 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        theRepository.addComponent(Component.Component("Dog", 4, 50))
        try:
            theRepository.estimateRelativeSize(name="Dog", methodCount=12, inputSize="M")                                        
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
    
    def test800_050_tooLittleDataShouldThrowException(self):
        expectedString = "Repository.estimateRelativeSize:" 
        maxCapacity = 100
        theRepository = Repository.Repository(maxCapacity)
        c = Component.Component("NonZero", 1, 10)
        theRepository.addComponent(c)
        try:
            theRepository.estimateRelativeSize("NonZero", 1, 10)                                         
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")

if __name__ == '__main__':
    unittest.main()