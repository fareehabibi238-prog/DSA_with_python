class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        arr=[]
        for i in nums1:
            if i in nums2:
                arr.append(i)
            if i in nums3:
                arr.append(i)
        for x in nums2:
            if x in nums1:
                arr.append(x)
            if x in nums3:
                arr.append(x)
        if arr:
            return list(set(arr))
        else:
            return []
        