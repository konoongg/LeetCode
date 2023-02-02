class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        nums2  = nums.copy()
        nums2.sort()
        left = 0
        right = len(nums2) - 1
        secondNum = 0
        firstNum = 0
        while left < right:
            summ = nums2[left] + nums2[right]
            if summ == target:
                firstNum = nums2[left]
                secondNum = nums2[right]
                break
            elif summ < target:
                left += 1
            else:
                right -= 1
        answer = []
        for i in range(len(nums)):
            if nums[i] == firstNum:
                answer.append(i)
                break
        for i in range(len(nums2)):
            if nums[i] == secondNum and i != answer[0] :
                answer.append(i)
                break
        return answer
