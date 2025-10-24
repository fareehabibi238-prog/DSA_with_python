class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr=[]
        midn=len(nums)//2
        left=nums[:midn]
        right=nums[midn:]
        leftn=0
        rightn=0
        for i in range(len(nums)):
            if i%2==0:
                if leftn<len(left):
                    arr.append(left[leftn])
                    leftn+=1
            else:
                if rightn<len(right):
                    arr.append(right[rightn])
                    rightn+=1
        return arr