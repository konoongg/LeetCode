class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rSum = sum(nums)
        lSum = 0
        for i, x in enumerate(nums):
            if rSum - x - lSum == lSum:
                return i
            lSum += x
        return -1

