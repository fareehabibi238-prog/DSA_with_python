class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        i=1
        newArray=[]
        while i<=n:
            if i%3==0 and i%5==0:
                newArray.append("FizzBuzz")
            elif i%3==0:
                newArray.append("Fizz")
            elif i%5==0:
                newArray.append("Buzz")
            else:
                newArray.append(str(i))
            i+=1
        return newArray
  