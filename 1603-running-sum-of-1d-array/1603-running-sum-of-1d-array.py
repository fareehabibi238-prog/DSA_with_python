class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr=[]
        count=0
        for i in nums:
            count+=i
            arr.append(count)
        return arr