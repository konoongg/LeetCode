class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        indexS = 0
        maxIndexS = len(s) 
        for i in t:
            if i == s[indexS]:
                indexS += 1
                if indexS == maxIndexS:
                    return True
        return False
