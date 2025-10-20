class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x=1
        m=0
        for d in  str(n):
            x*=int(d)
            m+=int(d)
        l=x+m
        if n%l==0:
            return True
        return False