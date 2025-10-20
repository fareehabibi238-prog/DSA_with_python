class Solution:
    def averageValue(self, nums: List[int]) -> int:
        x=0
        arr=[]
        for i in nums:
            if i%2==0:
                if i%3==0:
                    arr.append(i)
        if not arr:
           return 0
        return sum(arr) // len(arr)