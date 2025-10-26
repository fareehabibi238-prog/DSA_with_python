class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
            else:
                continue
        non=[x for x in nums if x !=0]
        zero=[x for x in nums if x==0]
        return non+zero

        