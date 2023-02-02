class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        isomorphicToS = {}
        isomorphicToT = {}
        for i in range(len(s)):
            if (s[i] not in isomorphicToT) and (t[i] not in isomorphicToS):
                isomorphicToT[s[i]] = t[i]
                isomorphicToS[t[i]] = s[i]
            elif (isomorphicToT.get(s[i]) != t[i]) or (isomorphicToS.get(t[i]) != s[i]):
                return False
        return True
