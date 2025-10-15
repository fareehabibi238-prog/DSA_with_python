class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        count=0
        count2=0
        while x<z or y>z:
            if x<z:
                x+=1
                count+=1
            if y>z:
                y-=1
                count2+=1
        while y<z or x>z:
            if y<z:
                y+=1
                count2+=1
            if x>z:
                x-=1
                count+=1
        if count<count2:
            return 1
        elif count>count2:
            return 2
        else:
            return 0
