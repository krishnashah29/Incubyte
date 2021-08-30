import unittest

class Tests_StringCalculator(unittest.TestCase):
    #1.
    def test_EmptyString_return_0(self):
        self.assertEqual(StringCalculator.Add(""),0)

     #1.1
    def test_SingleNumber(self):
        self.assertEqual(StringCalculator.Add("1"),1)
        self.assertEqual(StringCalculator.Add("2"),2)

class StringCalculator():
    def Add(self):
        #Empty String 
        if self=="":
            return 0
        
        #SingleNumbers
        if len(self)==1:
            return int(self)

if __name__=='__main__':
    unittest.main()