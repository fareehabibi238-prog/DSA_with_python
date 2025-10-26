class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count=0
        count2=0
        arr=[]
        for i in nums1:
            if i in nums2:
                count+=1
        for x in nums2:
            if x in nums1:
                count2+=1
        arr.append(count)
        arr.append(count2)
        return arr