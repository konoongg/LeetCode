class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minSize = 200
        for i in strs:
            if minSize > len(i):
                minSize = len(i)
        string = ""
        for i in range(minSize):
            flag = 0
            for j in strs:
                if j[i] != strs[0][i]:
                    flag = 1
                    break
            if flag == 0:
                string +=  strs[0][i]
            else:
                return string
        return string
