class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ms = []
        for i in range(1, n + 1):
            if(i % 3 == 0 and i % 5 == 0):
                ms.append("FizzBuzz")
            elif(i % 3 == 0 ):
                ms.append("Fizz")
            elif(i % 5 == 0 ):
                ms.append("Buzz")
            else:
                ms.append(str(i))
        return ms
''' 
    Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.
    https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/743/
'''