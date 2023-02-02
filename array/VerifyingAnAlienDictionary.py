class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderNum = {}
        for index, value in enumerate(order):
            orderNum[value] = index

        for i in range(len(words) -1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                if words[i][j] != words[i + 1][j]:
                    if orderNum[words[i][j]] > orderNum[words[i + 1][j]]:
                        return False
                    break
        return True
      
      """
      In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.
https://leetcode.com/problems/verifying-an-alien-dictionary/description/
      """
