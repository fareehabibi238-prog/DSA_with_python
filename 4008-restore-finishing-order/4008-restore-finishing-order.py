class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        array=[]
        for i in order:
            if i in friends:
                array.append(i)
        return array