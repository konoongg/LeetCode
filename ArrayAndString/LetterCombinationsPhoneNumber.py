class Solution:
    def returnCombinations(self, digits, size, status, returnArr, comb):
        if status == size:
            returnArr.append(comb)
        elif status < size:
            curIndex = int(digits[status]) - 2
            curNumber = self.numsToAlf[curIndex]
            for i in range(len(curNumber)):
                self.returnCombinations(digits, size, status + 1, returnArr, comb + curNumber[i])
        return returnArr


    def letterCombinations(self, digits: str) -> List[str]:
        self.numsToAlf = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],
        ['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        size = len(digits)
        if size == 0:
            return []
        elif size == 1:
            return self.numsToAlf[int(digits) - 2]
        returnArr = []
        return self.returnCombinations(digits, size, 0, returnArr, "")
