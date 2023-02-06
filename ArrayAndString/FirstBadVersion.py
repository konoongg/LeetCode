class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        left = 0
        right = n
        pvot = n // 2
        while left < right:
            if isBadVersion(pvot):
                right = pvot
            else:
                left = pvot + 1 
            pvot = (left + right) // 2
        return pvot
