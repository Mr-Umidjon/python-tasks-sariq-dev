import unittest
from doira import  getArea, getPerimeter

class DoiraTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(2), 12.56636, 6)
    
    def test_perimeter(self):
        self.assertAlmostEqual(getPerimeter(4), 25.13272)
        
unittest.main()
