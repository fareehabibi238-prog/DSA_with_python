class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
       x=2
       while True:
            if x%2==0 and x%n==0:
                return x
            x+=1 