class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        lastNum = 0
        for i in range(len(s) - 1 , -1, -1):
            num = 0
            if s[i] == 'I':
                num = 1
            elif s[i] == 'V':
                num = 5
            elif s[i] == 'X':
                num = 10
            elif s[i] == 'L':
                num = 50
            elif s[i] == 'C':
                num = 100
            elif s[i] == 'D':
                num = 500
            else:
                num = 1000
            if num >= lastNum:
                sum += num
            else:
                sum -= num
            lastNum = num
        return sum

    
