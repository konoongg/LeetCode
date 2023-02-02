class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        elif len(s) == 0:
            return True
        elif len(s) == 1:
            return s[0] == t[0]
        countS = [0] * 26
        countT = [0] * 26
        for i in range(len(s)):
            countS[ord(s[i]) - 97] += 1
            countT[ord(t[i]) - 97] += 1
        for i in range(26):
            if countS[i] != countT[i]:
                return False
        return True
