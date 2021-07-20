import unittest
from tubSonmi import tubSonmi

class tubSonTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(tubSonmi(23))
        self.assertTrue(tubSonmi(43))
        
    def test_false(self):
        self.assertFalse(tubSonmi(45))
        self.assertFalse(tubSonmi(24))
        self.assertFalse(tubSonmi(56))
        
unittest.main()