class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        result = -1
        for n in s:
            if -n in s and n > 0:
                result = max(result, n)
        return result