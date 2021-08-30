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
    
     #3.
    def test_NewLinesBetweenNumbers(self):
        self.assertEqual(StringCalculator.Add("4\n5,6"),15)
        
    #4.,10.(Delimiter any length)
    def test_DifferentDelimeters(self):
        self.assertEqual(StringCalculator.Add("//;\n1;2;3"),6)
        self.assertEqual(StringCalculator.Add("//##\n1##2##3##4##5"),15)
        self.assertEqual(StringCalculator.Add("//;#;\n1;#;2;#;3"),6)

class StringCalculator():
    global numbers
    numbers=[]
    def Add(self):
        #Empty String 
        if self=="":
            return 0
        
        #SingleNumbers
        if len(self)==1:
            return int(self)

        #NewLinesBetweenNumbers,NumbersWithComma
        if "," in self:
            if "\n" in self:
                return StringCalculator.NewLinesBetweenNumbers(self)
            
            return sum(StringCalculator.ExtractNumbers(self))
        
        #DifferentDelimiters
        if self.startswith("//"):
            return StringCalculator.MultipleDelimiters(self)

    
    def ExtractNumbers(self):
        numbers=self.split(',')
        numbers=[int(x) for x in numbers if int(x)<=1000]
        return numbers
    
    def NewLinesBetweenNumbers(self):

        for x in self:
            if x=="\n" or x==",":
                continue
            numbers.append(int(x))
        return sum(numbers)
    
    def MultipleDelimiters(self):
        
        delimiters,numbers=self.split("\n",1)
        numbers=numbers.split(delimiters[2:])
        numbers=[int(x) for x in numbers if int(x)<=1000]
        return sum(numbers)
    
    
if __name__=='__main__':
    unittest.main()