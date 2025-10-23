class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            array=[]
            for i in range(len(s)-1):
                sumDigit=(int(s[i])+int(s[i+1]))%10
                array.append(str(sumDigit))
            s="".join(array)
        return s[0]==s[1]