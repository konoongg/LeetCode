class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverseX = 0;
        X = x;
        while x > 0:
            reverseX *= 10
            reverseX += x % 10
            x //= 10
        if X != reverseX:
            return False
        return True
      #return str(x)==str(x)[::-1]))
