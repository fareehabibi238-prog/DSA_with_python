class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x=min(nums)
        y=max(nums)
        arr=[]
        for i in range(1,x+1):
            if x%i==0 and y%i==0:
                arr.append(i)

        return max(arr)