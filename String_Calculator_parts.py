import unittest

class Tests_StringCalculator(unittest.TestCase):
    #1.
    def test_EmptyString_return_0(self):
        self.assertEqual(StringCalculator.Add(""),0)

class StringCalculator():
    def Add(self):
        #Empty String 
        if self=="":
            return 0

if __name__=='__main__':
    unittest.main()