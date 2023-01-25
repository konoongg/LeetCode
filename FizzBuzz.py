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
        