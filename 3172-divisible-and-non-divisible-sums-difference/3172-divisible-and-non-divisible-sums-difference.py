class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
       total_sum=(n*(n+1))//2
       k=n//m
       div_sum=m*(k*(k+1))//2
       answer=total_sum-div_sum
       j=answer-div_sum
       return j