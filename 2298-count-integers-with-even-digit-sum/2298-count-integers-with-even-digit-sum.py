class Solution:
    def countEven(self, num: int) -> int:
       count = 0
       while num >= 2:
          digit_sum = sum(int(d) for d in str(num))
          if digit_sum % 2 == 0:
             count += 1
          num-= 1
       return count  