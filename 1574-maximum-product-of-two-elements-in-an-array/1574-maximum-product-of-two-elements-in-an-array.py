class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        arr=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                x=(nums[i]-1)*(nums[j]-1)
                arr.append(x)
        return max(arr)