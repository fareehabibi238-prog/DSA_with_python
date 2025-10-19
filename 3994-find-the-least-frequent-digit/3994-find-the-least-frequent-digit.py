class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        arr = []
        freq = {}
        digits = list(str(n))

        for i in digits:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        min_freq = min(freq.values())
        for d in digits:
            if freq[d] == min_freq:
                 arr.append(int(d))

        if arr:
            return min(arr)
        