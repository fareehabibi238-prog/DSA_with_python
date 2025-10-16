class Solution:
    def sumOfMultiples(self, n: int) -> int:
        array=[]
        while n>0:
            if (n%3==0) or (n%5==0) or (n%7==0):
                array.append(n)
            n-=1
        return sum(array)