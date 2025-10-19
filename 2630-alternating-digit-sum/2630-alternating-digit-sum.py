class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digit=[int(d) for d in str(n)]
        for i in range(len(digit)):
            if i%2==1:
                digit[i]=-digit[i]
        return sum(digit)