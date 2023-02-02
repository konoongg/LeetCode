class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        dividers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        strRoman = ['M', 'CM', 'D', 'CD', 'C', 'XC','L','XL', 'X', 'IX', 'V', 'IV' , 'I']
        for i in range(0, len(dividers)):
            div = dividers[i]
            roman += num // div * strRoman[i]
            num %= div
        return roman

