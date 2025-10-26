class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count=0
        count1=0
        for i in nums:
            if i !=0:
                if i>0:
                    count+=1
                else:
                    count1+=1
        return max(count,count1)