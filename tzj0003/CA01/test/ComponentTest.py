import unittest
from CA01.sandbox.Component import Component


class ComponentTest(unittest.TestCase):

    def instantiateComponent(self):
        Component("1", 3, 5)
        self.assertRaises(ValueError, Component, 1, 2, 3)
        self.assertRaises(ValueError, Component, "Test", -1, 4)
        self.assertRaises(ValueError, Component, "Test Again", 0, 0)            
    
    def retrieveName(self):
        comp = Component("2", 6, 9)
        name = comp.getName()
        self.assertEqual(name, "2")
        
    
    def retrieveMethodCount(self):
        comp = Component("3", 5, 10)
        mc = comp.getMethodCount()
        self.assertEqual(mc, 5)
        
    
    def retrieveLocCount(self):
        comp = Component("3", 2, 12)
        loc = comp.getLocCount()
        self.assertEqual(loc, 12)
        
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase('dummyTest')
    unittest.TextTestRunner(verbosity=2).run(suite)
        