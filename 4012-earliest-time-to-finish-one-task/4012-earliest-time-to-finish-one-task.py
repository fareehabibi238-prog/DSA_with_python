class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        sumRow=[sum(row) for row in tasks]
        return min(sumRow)