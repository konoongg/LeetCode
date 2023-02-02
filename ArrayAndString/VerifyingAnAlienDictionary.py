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
      

