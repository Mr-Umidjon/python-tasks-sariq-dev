import  unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_name(self):
        name = get_full_name("Ali", 'valiyev')
        self.assertEqual(name, 'Ali Valiyev')
    
    def test_otasi(self):
        name = get_full_name("ali", 'valiyev', 'husanovich')
        self.assertEqual(name, "Ali Husanovich Valiyev")
        
unittest.main()