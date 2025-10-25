class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=0
        count=nums[-1]
        for i in range(k):
            n+=count
            count+=1
        return n