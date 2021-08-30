import unittest

class Tests_StringCalculator(unittest.TestCase):
    #1.
    def test_EmptyString_return_0(self):
        self.assertEqual(StringCalculator.Add(""),0)

     #1.1
    def test_SingleNumber(self):
        self.assertEqual(StringCalculator.Add("1"),1)
        self.assertEqual(StringCalculator.Add("2"),2)
    
    #1.3
    def test_NumbersWithComma(self):
        self.assertEqual(StringCalculator.Add("4,5"),9)
        self.assertEqual(StringCalculator.Add("1,2,3"),6)
        self.assertEqual(StringCalculator.Add("1,2,3,4,5"),15)

class StringCalculator():
    def Add(self):
        #Empty String 
        if self=="":
            return 0
        
        #SingleNumbers
        if len(self)==1:
            return int(self)

        #NumbersWithComma
        if "," in self:
            return sum(StringCalculator.ExtractNumbers(self))

    
    def ExtractNumbers(self):
        numbers=self.split(',')
        numbers=[int(x) for x in numbers if int(x)<=1000]
        return numbers
if __name__=='__main__':
    unittest.main()