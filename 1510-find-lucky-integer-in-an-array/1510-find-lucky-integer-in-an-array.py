class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq={}
        num=[]
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for n in freq:
            if freq[n]==n:
               num.append(freq[n])
        if not num:
            return -1
        if len(num)<2:
            return num[0] if num else None
        else:
          return max(num)
        