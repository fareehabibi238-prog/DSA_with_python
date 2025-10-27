class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        x = nums2[0] - nums1[0]
        if all(a + x == b for a, b in zip(nums1, nums2)):
            return x
        else:
            raise ValueError("No consistent integer x makes nums1 equal to nums2.")
