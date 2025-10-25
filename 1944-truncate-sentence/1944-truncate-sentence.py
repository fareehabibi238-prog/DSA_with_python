class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        for i in s:
            x=(s.split()[:k])
        return" " .join(x)
        