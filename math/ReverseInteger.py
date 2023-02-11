class Solution:
    def reverse(self, x: int) -> int:
        
        isNegative = 0
        if x < 0:
            isNegative = 1
            x*= -1
        reverseInt = 0
        while x / 10  > 0:
            reverseInt *= 10
            reverseInt += x % 10
            x //= 10
        reverseInt += x % 10
        if isNegative:
            reverseInt *= -1
        if reverseInt < -2 ** 31 or reverseInt > 2**31 -1:
            return 0
        return reverseInt
            
        
