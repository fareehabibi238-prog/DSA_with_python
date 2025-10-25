class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count=0
        arr=[]
        for sentence in sentences:
            count=len(sentence.split())
            arr.append(count)
        return max(arr)