'''
Created on Nov 4, 2014

@author: Taylor
'''
import unittest
import CA04.prod.Iteration as Iteration
import CA04.prod.Project as Project

class Test(unittest.TestCase):
    
    def test100_010_shouldConstructProject(self):
        project = Project.Project()
        self.assertIsInstance(project, Project.Project)