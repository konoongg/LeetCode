class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        pvot = (left + right) // 2
        if target in nums:
            while nums[pvot] != target:
                if nums[pvot] < target:
                    left = pvot + 1
                    pvot = (left + right) // 2
                elif nums[pvot] > target:
                    right = pvot 
                    pvot = (left + right) // 2
            return pvot
        elif target < min(nums):
            return 0
        elif target > max(nums):
            return len(nums)
        else:
            while True:
                if nums[pvot] < target and nums[pvot + 1] > target:
                    return pvot + 1
                elif nums[pvot - 1] < target and nums[pvot] > target:
                    return pvot
                elif nums[pvot] < target:
                    left = pvot + 1
                    pvot = (left + right) // 2
                elif nums[pvot] > target:
                    right = pvot 
                    pvot = (left + right) // 2
                print(left, right)

