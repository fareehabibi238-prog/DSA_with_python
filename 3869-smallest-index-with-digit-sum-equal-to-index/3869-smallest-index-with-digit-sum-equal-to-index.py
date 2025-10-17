class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            digit_sum = sum(int(d) for d in str(abs(nums[i])))
            if digit_sum==i:
                return i
        return -1