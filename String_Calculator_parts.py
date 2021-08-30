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
    
    #5,6.
    def test_ExceptionForNegativeNumbers(self):
        self.assertRaises(Exception,StringCalculator.Add("-6"))
        self.assertRaises(Exception,StringCalculator.Add("-15,-6"))
        self.assertRaises(Exception,StringCalculator.Add("-15,-6,-1,-5"))
    
    #7. In StringCalculator Class
    #8. Not applicable here as its for .Net only
    #9.
    def test_NumberBigger_1000(self):
        self.assertEqual(StringCalculator.Add("//;#;\n1;#;2;#;3001"),3)
        self.assertEqual(StringCalculator.Add("1,2,3001"),3)

    #10.,11.,12.
    def test_MultipleDelimiters(self):
        self.assertEqual(StringCalculator.Add("//[***][%]\n1***2%3"),6)

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

        #NewLinesBetweenNumbers,NumbersWithComma,ExceptionNegativeNumbers,NumberBigger_1000
        if "," in self:
            if "\n" in self:
                return StringCalculator.NewLinesBetweenNumbers(self)
            
            result=sum(StringCalculator.ExtractNumbers(self))
            if result<0:
                return StringCalculator.Error(numbers)
            else:
                return result

        #MultipleDelimiters and DifferentDelimiters
        if self.startswith("//"):
            return StringCalculator.MultipleDelimiters(self)
        
        StringCalculator.AddCalledCount(StringCalculator.addcount)

    
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
        if self[2]!="[":
            delimiters,numbers=self.split("\n",1)
            numbers=numbers.split(delimiters[2:])
            numbers=[int(x) for x in numbers if int(x)<=1000]
            return sum(numbers)
        else:
            delimiters=StringCalculator.GetDelimiters(self)
            temp=self.split("\n",1)
            numbers=[]
            for d in delimiters:
                temp=temp[1].split(d)
                numbers.append(temp[0])
                numbers.append(temp[1])
            numbers=[int(x) for x in numbers if x.isdigit()]      
            return sum(numbers)


    def GetDelimiters(self):
        delimiters=[]
        temp=""
        for x in range(len(self)):
            if self[x]=="[":
                temp+=self[x+1]
                i=x+2
                while self[i]!="]" and i<=len(self):
                    temp+=self[i]
                    i+=1
                delimiters.append(temp)
                temp=""
        return delimiters
    
    def Error(self):
        try:
            Nnums=[x for x in self if x<'0']
            error_msg="Negative numbers are not allowed-"+Nnums
            raise Exception(error_msg)
        except Exception:
            pass
    
    
if __name__=='__main__':
    unittest.main()