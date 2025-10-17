class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        evenNum=[]
        oddNum=[]
        for i in range(1,n+1):
            evenNum.append(2*i)
            oddNum.append(2*i-1)
        if sum(evenNum)%n==0 and sum(oddNum)%n==0:
            return n