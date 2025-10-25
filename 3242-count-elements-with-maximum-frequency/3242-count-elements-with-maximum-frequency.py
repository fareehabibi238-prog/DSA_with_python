class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        count = 0

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        m = max(freq.values())

        for x in freq:
            if freq[x] == m:
                count += freq[x]

        return count