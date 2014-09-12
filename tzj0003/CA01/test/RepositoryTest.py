'''
Created on Sep 9, 2014

@author: Taylor
'''

import unittest
import CA01.prod.Repository as Repository
import CA01.prod.Comonent as Component

class RepositoryTest(unittest.TestCase):

    def setupTests(self):
        component1 = Component("Component01", 1, 76) 
        component2 = Component("Component02", 116, 4)
        component3 = Component("Component03", 7, 113)
        component4 = Component("Component04", 5, 103)
        component5 = Component("Component05", 0, 10)
        return [component1, component2, component3, component4, component5]
        

    def instaintiateRepository(self):
        repo = Respository(120)
        
    def addComponentToRepository(self):
        repo = Repository(130)
        comp = Component("Demo", 2, 30)
        count = repo.addComponent(comp)
        self.assertEqual(count, 1)
        
    def getCount(self):
        repo = Repository(13)
        comps = self.setupTests()
        for each in comps:
            repo.addComponent(each)
        vc = repo.count()
        self.assertEqual(vc, 5)
        
    
    def getValidCount(self):
        repo = Repository(13)
        comps = self.setupTests()
        for each in comps:
            repo.addComponent(each)
        vc = repo.validCount()
        self.assertEqual(vc, 4)
    
    def getRelativeSizes(self):
        repo = Repository(15)
        comps = self.setupTests()
        for each in comps:
            repo.addComponent(each)
        vc = repo.determineRelativeSizes()
        self.assetEqual(vc[0], 8)
        self.assertEqual(vc[1], 15)
        self.assertEqual(vc[2], 30)
        self.assertEqual(vc[3], 58)
        self.assertEqual(vc[4], 115)
        
    
        
        
        