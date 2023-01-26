class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        strX = str(x)
        for i in range (0, len(strX)):
            if strX[i] != strX[len(strX) - 1 -i]:
                return False
        return True