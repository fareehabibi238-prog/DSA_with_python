class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        array=[]
        for i in range(left,right+1):
            strNum=str(i)
            if "0" in strNum:
                continue
            if all(i%int(n)==0 for n in strNum):
                array.append(i)
        return array