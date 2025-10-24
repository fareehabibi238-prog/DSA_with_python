class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        array=[]
        for i in nums:
            if i%2==0:
                array.append(0)
            else:
                array.append(1)
        return sorted(array)