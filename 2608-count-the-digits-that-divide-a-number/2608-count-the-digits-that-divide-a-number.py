class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        for val in str(num):
            val=int(val)
            if val !=0 and num%val==0:
                count+=1
        return count