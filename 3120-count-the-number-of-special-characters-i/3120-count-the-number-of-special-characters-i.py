class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
       see=set(word)
       count=0
       for i in "abcdefghijklmnopqrstuvwxyz" :
        if i in see and  i.upper() in see:
            count+=1
       return count