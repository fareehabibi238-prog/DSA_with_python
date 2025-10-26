class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        arr=[]
        for i in range(len(nums)):
            if i%10==nums[i]:
                arr.append(i)
        if not arr:
          return -1
        if len(arr)<2:
            return arr[0] if arr else None
        else:
            return min(arr)
        