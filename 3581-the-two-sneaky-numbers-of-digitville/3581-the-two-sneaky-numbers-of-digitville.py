class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq={}
        arr=[]
        for i in nums:
            if i in freq:
                freq[i]+=1
                arr.append(i)
            else:
                freq[i]=1
        return arr