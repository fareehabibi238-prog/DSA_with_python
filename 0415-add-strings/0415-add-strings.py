class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0:
            d1 = int(num1[i]) if i >= 0 else 0
            d2 = int(num2[j]) if j >= 0 else 0

            x = d1 + d2 + carry
            if x >= 10:
                result.append(x % 10)
                carry = x // 10
            else:
                result.append(x)
                carry = 0

            i -= 1
            j -= 1

        if carry:
            result.append(carry)

        result.reverse()
        return "".join(str(d) for d in result)